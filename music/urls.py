from django.urls import path

from . import views

app_name = 'music'
urlpatterns = [
    path('', views.home, name='index'),
    path('add_song/', views.new_song, name='new_song'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlists/<int:playlist_id>', views.playlists_song, name='songsFromPlaylist'),
    path('songs/', views.songs, name='songs'),
]
"""path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('new_question/', views.new_question, name='new_question'),"""
