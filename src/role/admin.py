from __future__ import absolute_import

from django.contrib import admin
from .models import Role

class RoleAdmin(admin.ModelAdmin):
    pass

__all__ = ('RoleAdmin',)

admin.site.register(Role, RoleAdmin)
