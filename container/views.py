import datetime

import logging
from docker.errors import APIError, ImageNotFound
from oslo_i18n import translate as _

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContainerCreateForm
from .docorators import user_permission_container

from palamar.drivers.docker_api import ConnectDocker


@login_required
def index(request):
    return render(request, "container/index.html", {})


@login_required
def container_create(request):
    title = _("Create Container")
    subtitle = _("create a new container")
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    client_api = conn.docker_connect_api()
    images = client.images.list(all=True)
    networks = sorted(client_api.networks())
    if request.method == "POST":
        form = ContainerCreateForm(request.POST)
        if form.is_valid():
            title = _("Create Container")
            subtitle = _("create a new container")
            user_profile = request.user.profile
            conn = ConnectDocker(user_profile.selected_site)
            client = conn.docker_connect()
            client_api = conn.docker_connect_api()
            images = client.images.list(all=True)
            networks = sorted(client_api.networks())

            # define variables for container
            image = form.cleaned_data['image']
            command = form.cleaned_data['command']
            labels = {
                "site_id": str(user_profile.selected_site),
                "domain_id": str(user_profile.selected_domain),
                "project_id": str(user_profile.selected_project),
                "user_id": str(request.user.id)
            }
            name = form.cleaned_data['name']
            networking_config = client_api.create_networking_config({
                form.cleaned_data['network']: client_api.create_endpoint_config()
            })
            try:
                # create the container
                container = client_api.create_container(image,
                                                        command,
                                                        detach=True,
                                                        labels=labels,
                                                        name=name,
                                                        networking_config=networking_config, )
                # starts to container
                client_api.start(container)
                messages.success(request, _('Container "%s" created and started successfully' % name))
                return redirect('container-list')
            except APIError as error:
                logging.error(request, error)
                messages.error(request, error.explanation)
            except ImageNotFound as error:
                logging.error(request, error)
                messages.error(request, error.explanation)
            return render(request, "container/container_create.html", {"title": title,
                                                                       "subtitle": subtitle,
                                                                       "form": form,
                                                                       "images": images,
                                                                       "networks": networks, })
        else:
            print(form.errors)
    else:
        form = ContainerCreateForm()

    return render(request, "container/container_create.html", {"title": title,
                                                               "subtitle": subtitle,
                                                               "form": form,
                                                               "images": images,
                                                               "networks": networks, })


@login_required
def container_list(request):
    title = _("Manage Container")
    subtitle = _("create,list and manage containers")
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    containers = client.containers.list(all=True,
                                        filters={"label": ["domain_id=%s" % user_profile.selected_domain],
                                                 "label": ["project_id=%s" % user_profile.selected_project],
                                                 })
    current_date = datetime.datetime.now()

    return render(request, "container/container_list.html", {"containers": containers,
                                                             "title": title,
                                                             "subtitle": subtitle,
                                                             "current_date": current_date, })


@login_required
@user_permission_container
def container_start(request, container_id):
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    container = client.containers.get(container_id)
    container.start()
    messages.success(request, _('Container "%s" started!' % container.name))
    return redirect(request.META['HTTP_REFERER'])


@login_required
def container_stop(request, container_id):
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    container = client.containers.get(container_id)
    container.stop()
    messages.success(request, _('Container "%s" stopped!' % container.name))
    return redirect(request.META['HTTP_REFERER'])


@login_required
def container_remove(request, container_id):
    user_profile = request.user.profile
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    client_api = conn.docker_connect_api()
    container = client.containers.get(container_id)
    client_api.remove_container(container_id)
    messages.success(request, _('Container "%s" removed!' % container.name))
    return redirect(request.META['HTTP_REFERER'])
