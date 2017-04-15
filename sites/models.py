from __future__ import unicode_literals

import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings

# file storage
upload_storage = FileSystemStorage(location=settings.FILE_STORAGE)


class Sites(models.Model):
    name = models.CharField(max_length=64, null=True)
    url = models.CharField(max_length=512, null=True)
    client_cert = models.FileField(storage=upload_storage)
    client_key = models.FileField(storage=upload_storage)
    ssl_verify = models.BooleanField(default=True)
    ca_cert = models.FileField(storage=upload_storage)

    class Meta:
        verbose_name = ('Site')
        verbose_name_plural = ('Sites')
        ordering = ('name',)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.client_cert.path):
            os.remove(self.client_cert.path)
        if os.path.isfile(self.client_key.path):
            os.remove(self.client_key.path)
        if os.path.isfile(self.ca_cert.path):
            os.remove(self.ca_cert.path)

        super(Sites, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
