from __future__ import absolute_import

from django.db import models

from game.models import Game

__all__ = ('Member',)

class Member(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    title = models.CharField(max_length=254, blank=False, null=True)
    image = models.ImageField(upload_to='image/member', max_length=500)

    def __str__(self):
        return self.name
