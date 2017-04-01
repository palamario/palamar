import datetime


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dash_stack_dashboard.drivers.docker_api import ConnectDocker


@login_required
def index(request):
    return render(request, "container/index.html", {})

@login_required
def container_list(request):
    title = "Manage Container"
    subtitle = "create,list and manage containers"
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    containers = client.containers.list(all=True)
    current_date = datetime.datetime.now()

    return render(request, "container/container_list.html", {"containers": containers,
                                                             "title": title,
                                                             "subtitle": subtitle,
                                                             "current_date": current_date,})
