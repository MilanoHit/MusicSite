from django.contrib import admin
from MusicApp.models import MyMusicAppUser, Album, Review

@admin.register(MyMusicAppUser)
class MyUserAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")
    list_filter = ("email",)
    search_fields = ("email__startswith",)

@admin.register(Review)
class ReviewAdmin(admin. ModelAdmin):
    list_display = ("profile", "album")
    list_filter = ("profile",)
    search_fields = ("album__startswith", )

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
   list_display = ("album_name", "artist")
   list_filter = ("artist",)
   search_fields = ("artist__startswith", "album_name__startswith",)
