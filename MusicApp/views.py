from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from MusicApp.models import Album, MyMusicAppUser, Review
from MusicApp.forms import LoginForm, MyMusicAppCreationForm, AddAlbumForm, ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.list import ListView
from django.core.paginator import Paginator


def home(request):
    albums = Album.objects.all()
    user = request.user.is_authenticated
    context = {
        'albums': albums,
        'user': user,
    }
    return render(request, template_name='home-no-profile.html', context=context)


class AddAlbum(views.CreateView, LoginRequiredMixin):
    model = Album
    form_class = AddAlbumForm
    template_name = 'add-album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.profile = self.request.user
        # article.save()  # This is redundant, see comments.
        return super(AddAlbum, self).form_valid(form)





class ProfileDetails(views.DetailView):
    pass


class Register(views.CreateView):
    model = MyMusicAppUser

    form_class = MyMusicAppCreationForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('login')


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    next_page = reverse_lazy('home')


class Logout(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class ReviewAlbum(views.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.profile = self.request.user
        review.album = Album.objects.get(id=self.kwargs.get('pk'))
        return super(ReviewAlbum, self).form_valid(form)



# def AlbumsShowcase(request):
#     albums = Album.objects.all()
#     context = {
#         'albums': albums
#     }
#     return render(request, template_name='albums-showcase.html', context=context)


class AlbumListView(ListView):
    model = Album
    template_name = 'albums-showcase.html'
    context_object_name = 'albums'
    paginate_by = 10  # Number of albums per page

    def get_queryset(self):
        return Album.objects.all()  # Retrieve all albums