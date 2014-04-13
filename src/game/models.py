from __future__ import absolute_import

from django.db import models

__all__ = ('Game', 'DownloadType', 'Snapshot', 'Genre')


class Genre(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=254, blank=False)
    image = models.ImageField(upload_to='image/game', max_length=500)
    description = models.CharField(max_length=2000, blank=False)
    genre_set = models.ManyToManyField(Genre, null=True)

    def __str__(self):
        return self.name

class Snapshot(models.Model):
    game = models.ForeignKey(Game)
    image = models.ImageField(upload_to='image/game/snapshot', max_length=500)

    def __str__(self):
        return self.game.name

GAME_TYPE_CHOISES = (
    ('MAC', 'Mac OS X'),
    ('WIN', 'MS Windows'),
    ('WEB', 'Play on web'),
    ('IOS', 'iOS'),
    ('AND', 'Android'),
    ('ETC', 'etc.'),
)


class DownloadType(models.Model):
    game = models.ForeignKey(Game)
    link = models.URLField()
    platform = models.CharField(max_length=3, choices=GAME_TYPE_CHOISES)

    def __str__(self):
        return self.game.name + ' - ' + self.platform
