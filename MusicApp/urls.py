from django.contrib import admin
from django.urls import path
from MusicApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('album/add/', views.AddAlbum.as_view(), name="add-album"),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('album/detail/<int:pk>/', views.album_details, name="album-details"),
    path('album/edit/<int:pk>/', views.EditAlbum.as_view(), name="album-edit"),
    path('album/delete/<int:pk>/', views.AlbumDeleteView.as_view(), name="album-delete"),
    path('profile/details/<int:id>/', views.profile_details, name="profile-details"),
    path('profile/edit/<int:pk>/', views.UserEdit.as_view(), name="profile-edit"),
    path('profile/delete/<int:pk>/', views.ProfileDeleteView.as_view(), name="profile-delete"),
    path('album/review/<int:pk>/', views.ReviewAlbum.as_view(), name='review'),
    path('album/reviews/<int:pk>/', views.ReviewsListView.as_view(), name='review-list'),
    path('albums/', views.AlbumListView.as_view(), name='showcase'),
    path('review/<int:pk>/like/', views.like_review, name='like-review'),
    path('review/<int:pk>/dislike/', views.dislike_review, name='dislike-review'),
]
