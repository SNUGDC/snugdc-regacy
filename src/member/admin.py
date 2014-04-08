from __future__ import absolute_import

from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    pass

__all__ = ('MemberAdmin',)

admin.site.register(Member, MemberAdmin)
