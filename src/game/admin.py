from __future__ import absolute_import

from django.contrib import admin
from .models import Game, DownloadType

class GameAdmin(admin.ModelAdmin):
    pass

class DownloadTypeAdmin(admin.ModelAdmin):
    pass

__all__ = ('GameAdmin', 'DownloadTypeAdmin')

admin.site.register(Game, GameAdmin)
admin.site.register(DownloadType, DownloadTypeAdmin)
