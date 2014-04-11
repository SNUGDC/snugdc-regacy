from __future__ import absolute_import

from django.db import models

__all__ = ('Game', 'DownloadType')

class Game(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    image = models.ImageField(upload_to='images/game', max_length=500)
    description = models.CharField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.name



GAME_TYPE_CHOISES = (
    ('MAC', 'Mac OS X'),
    ('WIN', 'MS Windows'),
    ('WEB', 'Play on web'),
    ('IOS', 'iOS'),
    ('AND', 'Android'),
    ('SRC', 'Source'),
)

class DownloadType(models.Model):
    game = models.ForeignKey(Game)
    link = models.URLField()
    platform = models.CharField(max_length=3, choices=GAME_TYPE_CHOISES, null=True)

    def __str__(self):
        return self.platform
