from __future__ import absolute_import

from django.contrib import admin
from .models import Participation

class ParticipationAdmin(admin.ModelAdmin):
    pass

__all__ = ('ParticipationAdmin',)

admin.site.register(Participation, ParticipationAdmin)
