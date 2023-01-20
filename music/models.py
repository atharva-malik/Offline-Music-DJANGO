from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    title = models.TextField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Create your models here.
class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    #duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title


class Song_name(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
