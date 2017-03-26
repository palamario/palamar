from oslo_i18n import translate as _

from django import forms

from .models import Sites


class SiteEditForm(forms.Form):
    name=forms.CharField(
        label=_('Name'),
        max_length=64
    )
    url=forms.CharField(
        label=_('URL'),
        max_length=512
    )
    client_cert=forms.FileField(
        label=_('Client Certificate')
    )
    client_key=forms.FileField()
    ca_cert=forms.FileField()
    ssl_verify=forms.BooleanField()

    class Meta:
        model=Sites
        fields=('name', 'url', 'client_cert', 'client_key', 'ca_cert', 'ssl_verify')