from __future__ import absolute_import

from django.db import models

__all__ = ('Game',)

GAME_TYPE_CHOISES = (
    ('DLC', 'Downloadable content'),
    ('WEB', 'Play on web')
)

class Game(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    play_link = models.URLField(null=True)
    image = models.URLField(null=True)
    description = models.CharField(max_length=2000, blank=False, null=False)
    game_type = models.CharField(max_length=3, choices=GAME_TYPE_CHOISES)

    def __str__(self):
        return self.name
