from oslo_i18n import translate as _

from django import forms
from . models import Sites


class SiteCreateForm(forms.Form):
    name=forms.CharField(
        label=_('Name'),
        max_length=64,
        required=True
    )
    url=forms.CharField(
        label=_('URL'),
        max_length=512,
        required=True
    )
    client_cert=forms.FileField(
        label=_('Client Certificate'),
        required=True
    )
    client_key=forms.FileField(
        label=_('Client Key'),
        required=True
    )
    ca_cert=forms.FileField(
        label=_('CA Certificate'),
        required=True
    )
    ssl_verify=forms.BooleanField(
        label=_('Verify SSL'),
        required=False
    )

class SiteEditForm(forms.Form):
    name=forms.CharField(
        label=_('Name'),
        max_length=64,
        required=True
    )
    url=forms.CharField(
        label=_('URL'),
        max_length=512,
        required=True
    )
    client_cert=forms.FileField(
        label=_('Client Certificate'),
        required=False
    )
    client_key=forms.FileField(
        label=_('Client Key'),
        required=False
    )
    ca_cert=forms.FileField(
        label=_('CA Certificate'),
        required=False
    )
    ssl_verify=forms.BooleanField(
        label=_('Verify SSL'),
        required=False
    )