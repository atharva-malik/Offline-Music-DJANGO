from django.contrib import admin
from . models import Song, Playlist, Song_name

# Register your models here.
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Song_name)
