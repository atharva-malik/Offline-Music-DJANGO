from django import forms
from . import models
import os

# INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 32)]
#SONG_CHOICES = [tuple([x.replace('.mp3', ''), x.replace('.mp3', '')]) for x in os.listdir("C:\\Atharva\\Progr"
#                                                                                          "amming\\Python\\Py"
#                                                                                          "thon Scripts\\DJAN"
#                                                                                          "GO\\offline_music"
#                                                                                         "\\media")]

SONG_CHOICES = [tuple([x, x]) for x in models.Song_name.objects.all().values_list('title')]
SONG_CHOICES = []
for x in models.Song_name.objects.all().values_list('title'):
    SONG_CHOICES.append(tuple([x[0], x[0]]))


PLAYLIST_CHOICES = [tuple([x, x]) for x in models.Playlist.objects.all()]


# PLAYLIST_CHOICES.append(tuple(["Create a playlist", "Create a playlist"]))


class UserForm(forms.Form):
    song = forms.CharField(label='Which song would you like to add?',
                                     widget=forms.Select(choices=SONG_CHOICES))
    Playlist = forms.CharField(label="Which playlist will you add this to?(It will create one if it does not exist)",)
                               # widget=forms.Select(choices=PLAYLIST_CHOICES),
#    if Playlist == "Create a playlist":
#        playlist_name = forms.CharField(max_length=100)
