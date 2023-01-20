from django import forms


class SongNameForm(forms.Form):
    song_name = forms.CharField(label='Song name', max_length=75)
