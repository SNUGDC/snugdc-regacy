from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from game.models import Game

__all__ = ('Member',)

class Member(models.Model):
    username = models.CharField(max_length=254, blank=False, null=False)
    title = models.CharField(max_length=254, blank=False, null=True)
    image = models.ImageField(upload_to='images/member', max_length=500)
