from django.contrib import admin
from MusicApp.models import MyMusicAppUser, Album, Review

@admin.register(MyMusicAppUser)
class MyUserAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

