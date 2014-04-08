from __future__ import absolute_import

from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    pass

__all__ = ('GameAdmin',)

admin.site.register(Game, GameAdmin)
