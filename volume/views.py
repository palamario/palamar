import datetime
import logging
from oslo_i18n import translate as _


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages


from palamar.drivers.docker_api import ConnectDocker

@login_required
def index(request):
    return render(request, "volume/index.html", {})


@login_required
def volume_list(request):
    title = _("Manage Volume")
    subtitle = _("create,list and manage volumes")
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect_api()
    volumes = client.volumes()


    return render(request, "volume/volume_list.html", {"volumes": volumes,
                                                         "title": title,
                                                         "subtitle": subtitle,})