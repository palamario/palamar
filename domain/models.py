from __future__ import unicode_literals

from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=64,
                            db_index=True,
                            unique=True)
    enabled = models.BooleanField(default=True)
    extra = models.TextField(default="{}")

    def __str__(self):
        return self.name