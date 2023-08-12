from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from MusicApp.models import Album, MyMusicAppUser, Review, Like, Dislike
from MusicApp.forms import LoginForm, MyMusicAppCreationForm, AddAlbumForm, ReviewForm, MyMusicAppUserEdit
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin
import json


class CanDeleteAlbumMixin(UserPassesTestMixin):
    def test_func(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return self.request.user.has_perm('MusicApp.can_delete_album')


def home(request):
    albums = Album.objects.all()
    user = request.user.is_authenticated
    albums_json = json.dumps(list(albums.values('album_name', 'image')))  # Customize fields as needed
    context = {
        'albums': albums,
        'user': user,
        'albums_json': albums_json,
    }
    return render(request, template_name='home-no-profile.html', context=context)


class AddAlbum(LoginRequiredMixin, views.CreateView):
    model = Album
    form_class = AddAlbumForm
    template_name = 'add-album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.profile = self.request.user
        return super(AddAlbum, self).form_valid(form)


class EditAlbum(LoginRequiredMixin, views.UpdateView):
    model = Album
    form_class = AddAlbumForm
    template_name = 'edit-album.html'

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.id})


@login_required
def album_details(request, pk):
    album = Album.objects.get(id=pk)
    context = {
        'album': album
    }
    return render(request, template_name='album-details.html', context=context)



class AlbumDeleteView(CanDeleteAlbumMixin, LoginRequiredMixin, views.DeleteView):
    model = Album
    template_name = 'album-delete.html'
    success_url = reverse_lazy('home')




class Register(views.CreateView):
    model = MyMusicAppUser

    form_class = MyMusicAppCreationForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('login')


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    next_page = reverse_lazy('home')


class UserEdit(LoginRequiredMixin, views.UpdateView):
    model = MyMusicAppUser
    form_class = MyMusicAppUserEdit
    template_name = 'edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'id':self.object.id})


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    model = MyMusicAppUser
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('home')



@login_required
def profile_details(request, id):
    profile = MyMusicAppUser.objects.get(id=id)
    context = {
        'profile': profile
    }
    return render(request, template_name='profile-details.html', context=context)


class Logout(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('home')


class ReviewAlbum(LoginRequiredMixin, views.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.profile = self.request.user
        review.album = Album.objects.get(id=self.kwargs.get('pk'))
        return super(ReviewAlbum, self).form_valid(form)

class ReviewsListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'review-showcase.html'
    context_object_name = 'reviews'
    paginate_by = 3

    def get_queryset(self):
        album = Album.objects.get(id=self.kwargs.get('pk'))
        reviews = Review.objects.filter(album=album)
        return reviews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = Album.objects.get(id=self.kwargs.get('pk'))
        context['album'] = album  # Add album object to context
        return context



class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums-showcase.html'
    context_object_name = 'albums'
    paginate_by = 3  # Number of albums per page

    def get_queryset(self):
        albums = Album.objects.all()

        # Calculate average rating for each album
        for album in albums:
            reviews = Review.objects.filter(album=album)
            total_ratings = sum(int(review.rating) for review in reviews)
            if reviews:
                album.average_rating = total_ratings / len(reviews)
            else:
                album.average_rating = 0  # No reviews

        return albums


@login_required
def like_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    like = Like.objects.filter(profile=request.user, review=review).first()
    dislike = Dislike.objects.filter(profile=request.user, review=review).first()

    if like:
        like.delete()
    elif dislike:
        dislike.delete()
        Like.objects.create(profile=request.user, review=review)
    else:
        Like.objects.create(profile=request.user, review=review)

    return redirect('review-list', pk=review.album.id)



@login_required
def dislike_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    dislike = Dislike.objects.filter(profile=request.user.id, review=review).first()
    like = Like.objects.filter(profile=request.user.id, review=review).first()

    if dislike:
        dislike.delete()
    elif like:
        like.delete()
        Dislike.objects.create(profile=request.user, review=review)
    else:
        Dislike.objects.create(profile=request.user, review=review)

    return redirect('review-list', pk=review.album.id)