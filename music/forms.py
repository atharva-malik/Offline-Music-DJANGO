from django import forms
from . import models

SONG_CHOICES = [tuple([x, x]) for x in models.Song_name.objects.all().values_list('title')]
SONG_CHOICES = []
for x in models.Song_name.objects.all().values_list('title'):
    SONG_CHOICES.append(tuple([x[0], x[0]]))


PLAYLIST_CHOICES = [tuple([x, x]) for x in models.Playlist.objects.all()]


class UserForm(forms.Form):
    song = forms.CharField(label='Which song would you like to add?',
                                     widget=forms.Select(choices=SONG_CHOICES))
    Playlist = forms.CharField(label="Which playlist will you add this to?(It will create one if it does not exist)",)
