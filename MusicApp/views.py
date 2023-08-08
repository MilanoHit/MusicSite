from django.shortcuts import render, redirect
from django.views import generic as views
from MusicApp.models import Album, MyMusicAppUser
from MusicApp.forms import LoginForm, MyMusicAppCreationForm, AddAlbumForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


def home(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, template_name='home-no-profile.html', context=context)


class AddAlbum(views.CreateView):
    model = Album
    form_class = AddAlbumForm
    template_name = 'add-album.html'
    success_url = reverse_lazy('home')


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