from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from MusicApp.models import Album, MyMusicAppUser, Review
from MusicApp.forms import LoginForm, MyMusicAppCreationForm, AddAlbumForm, ReviewForm, MyMusicAppUserEdit
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.core.paginator import Paginator


def home(request):
    albums = Album.objects.all()
    user = request.user.is_authenticated
    context = {
        'albums': albums,
        'user': user,
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

@login_required
def profile_details(request, id):
    profile = MyMusicAppUser.objects.get(id=id)
    context = {
        'profile': profile
    }
    return render(request, template_name='profile-details.html', context=context)


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

