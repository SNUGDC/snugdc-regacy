from __future__ import absolute_import

from django.db import models

__all__ = ('Role',)


class Role(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
