import datetime
from oslo_i18n import translate as _


from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages


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

@login_required
def container_start(request,container_id):
    user_profile = request.user.profile
    conn=ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    container = client.containers.get(container_id)
    container.start()
    messages.success(request, _('Container "%s" started!' % container.name))
    return redirect(request.META['HTTP_REFERER'])


@login_required
def container_stop(request,container_id):
    user_profile = request.user.profile
    conn=ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    container = client.containers.get(container_id)
    container.stop()
    messages.success(request, _('Container "%s" stopped!' % container.name))
    return redirect(request.META['HTTP_REFERER'])

@login_required
def container_remove(request,container_id):
    user_profile = request.user.profile
    conn=ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    client_api = conn.docker_connect_api()
    container = client.containers.get(container_id)
    client_api.remove_container(container_id)
    messages.success(request, _('Container "%s" removed!' % container.name))
    return redirect(request.META['HTTP_REFERER'])