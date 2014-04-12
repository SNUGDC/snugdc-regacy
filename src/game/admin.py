from __future__ import absolute_import

from django.contrib import admin
from .models import Game, DownloadType, Genre

class GameAdmin(admin.ModelAdmin):
    pass

class DownloadTypeAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

__all__ = ('GameAdmin', 'DownloadTypeAdmin', 'GenreAdmin')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(DownloadType, DownloadTypeAdmin)
