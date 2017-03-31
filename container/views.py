from oslo_i18n import translate as _

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from dash_stack_dashboard.drivers.docker_api import ConnectDocker


@login_required
def index(request):
    return render(request, "container/index.html", {})

@login_required
def container_list(request):
    title="Manage Container"
    subtitle="create,list and manage containers"
    conn=ConnectDocker(3)
    client=conn.docker_connect()
    containers=client.containers.list(all=True)


    return render(request, "container/container_list.html", {"containers": containers,
                                                     "title": title,
                                                     "subtitle": subtitle,})