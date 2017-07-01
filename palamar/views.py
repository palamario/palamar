import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user_profile.models import Profile

@login_required
def index(request):
    user_profile = Profile.objects.filter(user=request.user)

    if user_profile[0].selected_project < 1:
        # User has no project
        return redirect("create-project")

    return render(request, "base.html", {'time' : datetime.datetime.now()})