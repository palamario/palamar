from oslo_i18n import translate as _

from django import forms

class ProjectForm(forms.Form):
    project = forms.CharField(
        label=_('Project Name'),
        required=True,
        error_messages={'required': _('Please enter your project name!')}
    )
    tos = forms.BooleanField(
        required=True,
        error_messages={'required': _('You must accept TOS.')}
    )
