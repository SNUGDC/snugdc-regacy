from __future__ import absolute_import

from django.db import models
from member.models import Member
from game.models import Game
from role.models import Role

__all__ = ('Participation',)

class Participation(models.Model):
    member = models.ForeignKey(Member)
    game = models.ForeignKey(Game)
    roles = models.ManyToManyField(Role)

    class Meta:
        unique_together = ('member', 'game')
