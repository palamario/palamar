from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from user_profile.models import Profile

@login_required
def project_select(request,project_id,user_id):
    user = Profile.objects.get(user_id=user_id)
    user.selected_project = project_id
    user.save()
    return redirect(request.META['HTTP_REFERER'])