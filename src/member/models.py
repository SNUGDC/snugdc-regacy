from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from game.models import Game

__all__ = ('Member',)


class MemberManager(BaseUserManager):
    def create_user(self, username, title, image):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            username=username
        )
        if title:
            user.title = title
        if image:
            user.image = image
        user.is_admin = False
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    username = models.CharField(max_length=254, blank=False, null=False)
    title = models.CharField(max_length=254, blank=False, null=True)
    is_admin = models.BooleanField(default=False)
    image = models.URLField(null=True)
    objects = MemberManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
