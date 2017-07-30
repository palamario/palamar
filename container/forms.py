from oslo_i18n import translate as _
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from cuser.middleware import CuserMiddleware

from django import forms

from domain.models import Domain
from project.models import Project
from user_profile.models import Profile

from palamar.drivers.docker_api import ConnectDocker


class ContainerCreateForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        required=True,
    )
    image = forms.CharField(
        label=_('Image'),
        required=True
    )
    command = forms.CharField(
        label=_('Command'),
        required=True
    )
    network = forms.CharField(
        label=_('Network'),
        required=True
    )
