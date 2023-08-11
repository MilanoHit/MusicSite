from django.contrib import admin
from django.urls import path
from MusicApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('album/add/', views.AddAlbum.as_view(), name="add-album"),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    # path('album/detail/<int:id>/', views.album_details, name="album-details"),
    # path('album/edit/<int:id>/', views.album_edit, name="album-edit"),
    # path('album/delete/<int:id>/', views.album_delete, name="album-delete"),
    path('profile/details/<int:id>/', views.profile_details, name="profile-details"),
    path('profile/edit/<int:pk>/', views.UserEdit.as_view(), name="profile-edit"),
    # path('profile/delete/', views.profile_delete, name="profile-delete"),
    path('album/review/<int:pk>/', views.ReviewAlbum.as_view(), name='review'),
    path('albums/', views.AlbumListView.as_view(), name='showcase')
]
