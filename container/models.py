from __future__ import unicode_literals

from django.db import models

class Quota(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    project = models.IntegerField(null=True)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField()

