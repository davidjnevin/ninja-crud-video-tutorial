from django.db import models


class Track(models.Model):
    """Track."""

    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()
