import logging

from oslo_i18n import translate as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from user_profile.models import Profile
from project.models import Project


@login_required
def domain_select(request,domain_id, user_id):
    project = Project.objects.filter(domain_id=domain_id).first()
    user = Profile.objects.get(user_id=user_id)
    user.selected_domain = domain_id
    try:
        user.selected_project = project.id
    except:
        user.selected_project = None
        logging.warning(_('Domain does not have any project!'))
        messages.warning(request, 'Domain does not have any project!')
    user.save()
    return redirect(request.META['HTTP_REFERER'])