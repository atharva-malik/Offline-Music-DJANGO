# from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
# from os import listdir, path, getcwd
from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.http import Http404
from .models import Song, Playlist
from . import forms

# from django.core.paginator import Paginator
# from django.urls import reverse
# from django.template import loader
# from django.views import generic

# Create your views here.
"""
@login_required
def home(request):
    return render(request, "music/home.html", context={'filenames': listdir("C:\\Atharva\\Programming\\Python\\Python "
                                                                            "Scripts\\DJANGO\\offline_music\\media")})
def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)
"""


@login_required
def new_song(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            if Song.objects.filter(title=form.cleaned_data["song"], user=request.user):
                raise PermissionDenied(
                    "You have already added that song!"
                )
            try:
                s = Song(user=request.user, title=form.cleaned_data["song"],
                         playlist=Playlist.objects.filter(title=form.cleaned_data["Playlist"],
                                                          user_name=request.user)[0])
                s.save()
            except IndexError:
                p = Playlist(title=form.cleaned_data["Playlist"], user_name=request.user)
                p.save()
                s = Song(user=request.user, title=form.cleaned_data["song"],
                         playlist=Playlist.objects.filter(title=form.cleaned_data["Playlist"],
                                                          user_name=request.user)[0])
                s.save()
            return HttpResponseRedirect('/music/')
    else:
        form = forms.UserForm()
    return render(request, 'music/new_song.html', context={"form": form})


@login_required
def home(request):
    return render(request, "music/home.html")


def playlists(request):
    return render(request, "music/playlists.html", context={"playlists": Playlist.objects.filter(user_name=request.user)})


def playlists_song(request, playlist_id):
    answers_list = list(Song.objects.filter(playlist=playlist_id).values_list('title'))
    songlist = ""
    songNameList = ""
    length = len(answers_list)
    number = 1
    for answer in answers_list:
        if number < length:
            songlist += answer[0] + ","
            songNameList += answer[0] + ","
            number += 1
        else:
            songlist += answer[0]
            songNameList += answer[0]
    songlist = songlist.replace(" ", "").replace("'", "")

    return render(request, "music/playlist_song.html", context={"songlist": songlist, "songNameList": songNameList})


def songs(request):
    answers_list = list(Song.objects.filter(user=request.user).values_list('title'))
    songlist = ""
    songNameList = ""
    length = len(answers_list)
    number = 1
    for answer in answers_list:
        if number < length:
            songlist += answer[0] + ","
            songNameList += answer[0] + ","
            number += 1
        else:
            songlist += answer[0]
            songNameList += answer[0]
    songlist = songlist.replace(" ", "").replace("'", "")

    return render(request, "music/songs.html", context={"songlist": songlist, "songNameList": songNameList})
