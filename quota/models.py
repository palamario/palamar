from __future__ import unicode_literals

from django.db import models

from domain.models import Domain
from project.models import Project

class Resources(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    type = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.name

class Quotas(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    project = models.ForeignKey(Project)
    domain = models.ForeignKey(Domain, null=True)
    resource = models.ForeignKey(Resources)
    hard_limit = models.IntegerField(null=True)
    allocated = models.IntegerField(null=True)

    def __int__(self):
        return self.id


class Classes(models.Model):
    name = models.DateTimeField(max_length=32, db_index=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    resource = models.ForeignKey(Resources)
    hard_limit = models.IntegerField()

    def __str__(self):
        return self.name


class Usages(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    project = models.ForeignKey(Project)
    domain = models.ForeignKey(Domain, null=True)
    resource = models.ForeignKey(Resources)
    in_use = models.IntegerField()
    reserved = models.IntegerField()
    until_refresh = models.IntegerField()

    def __int__(self):
        return self.id


class Reservations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    usage = models.ForeignKey(Usages)
    project = models.ForeignKey(Project)
    domain = models.ForeignKey(Domain, null=True)
    resource = models.ForeignKey(Resources)
    expire = models.DateTimeField()
    allocated = models.ForeignKey(Quotas)

    def __int__(self):
        return self.id
