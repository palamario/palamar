import logging

from oslo_i18n import translate as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from user_profile.models import Profile
from project.models import Project
from role.models import Assignment


@login_required
def domain_select(request,domain_id, user_id):
    user = Profile.objects.get(user_id=user_id)
    user.selected_domain = domain_id
    assigned_projects = Assignment.objects.filter(type=1,
                                         actor=user_id,
                                         target_domain_id=user.selected_domain)
    assigned_project = assigned_projects.first()
    # try to assign first project as selected project.
    # if there is no project for domain, raise exception and assign none to selected_project
    if assigned_project:
        user.selected_project = assigned_project.target_project_id
    else:
        user.selected_project = None
        logging.warning(_('Domain does not have any project!'))
        messages.warning(request, 'Domain does not have any project!')
    user.save()
    return redirect(request.META['HTTP_REFERER'])