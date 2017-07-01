import datetime
import logging
from oslo_i18n import translate as _


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages


from palamar.drivers.docker_api import ConnectDocker

@login_required
def index(request):
    return render(request, "image/index.html", {})


def image_list(request):
    title = _("Manage Images")
    subtitle = _("create,list and manage images")
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    images = client.images.list(all=True)


    return render(request, "image/image_list.html", {"images": images,
                                                             "title": title,
                                                             "subtitle": subtitle,})