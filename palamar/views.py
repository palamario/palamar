import datetime
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from role.models import Assignment
from user_profile.models import Profile

@login_required
def index(request):
    user_profile = Profile.objects.filter(user=request.user)

    selected_project = user_profile[0].selected_project

    if selected_project > 0:
        assignments = Assignment.objects.filter(actor=request.user.id, target_project=selected_project)
        if len(assignments) > 0:
            logging.info("User has logged in.")
            return render(request, "base.html", {'time' : datetime.datetime.now()})

    # User has no project
    logging.info("User has no default project. Redirecting to create project page.")
    return redirect("create-project")