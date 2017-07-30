import datetime
import logging
from oslo_i18n import translate as _


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages


from palamar.drivers.docker_api import ConnectDocker

@login_required
def index(request):
    return render(request, "network/index.html", {})

@login_required
def network_list(request):
    title = _("Manage Network")
    subtitle = _("create,list and manage networks")
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect_api()
    networks = client.networks()
    networks = sorted(networks)

    return render(request, "network/network_list.html", {"networks": networks,
                                                         "title": title,
                                                         "subtitle": subtitle,})