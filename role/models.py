from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from domain.models import Domain
from project.models import Project


class Role(models.Model):
    name = models.CharField(max_length=32)
    extra = models.TextField()

    def __str__(self):
        return self.name

class Assignment(models.Model):

    ASSIGNMENT_TYPES = ((1, 'UserProject'),
                        (2, 'GroupProject'),
                        (3, 'UserDomain'),
                        (4, 'GroupDomain'),)

    type = models.IntegerField(null=True, choices=ASSIGNMENT_TYPES)
    actor = models.ForeignKey(User)
    target_domain = models.ForeignKey(Domain, null=True, blank=True)
    target_project = models.ForeignKey(Project, null=True, blank=True)
    role = models.ForeignKey(Role)

    def __int__(self):
        return self.id
