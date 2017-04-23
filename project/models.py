from __future__ import unicode_literals

from django.db import models

from domain.models import Domain


class Project(models.Model):
    name = models.CharField(max_length=64, db_index=True, unique=True)
    extra = models.TextField(default="{}")
    description = models.TextField()
    enabled = models.BooleanField(default=True)
    domain = models.ForeignKey(Domain, db_index=True, default=1)

    def __str__(self):
        return self.name