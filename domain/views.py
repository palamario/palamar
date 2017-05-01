from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from user_profile.models import Profile


@login_required
def domain_select(request,domain_id, user_id):
    u = Profile.objects.get(user_id=user_id)
    u.selected_domain = domain_id
    u.save()
    return redirect(request.META['HTTP_REFERER'])