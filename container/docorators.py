import logging

from django.shortcuts import redirect
from oslo_i18n import translate as _

from django.contrib import messages
from palamar.drivers.docker_api import ConnectDocker


def container_permission_required(function):
    def wrap(request, *args, **kwargs):
        user_profile = request.user.profile
        conn = ConnectDocker(user_profile.selected_site)
        client = conn.docker_connect()
        client_api = conn.docker_connect_api()
        container = client.containers.get(kwargs['container_id'])
        site_id = int(container.attrs['Config']['Labels']['site_id'])
        domain_id = int(container.attrs['Config']['Labels']['domain_id'])
        project_id = int(container.attrs['Config']['Labels']['project_id'])
        if (user_profile.selected_site == site_id and
            user_profile.selected_domain == domain_id and
            user_profile.selected_project == project_id):
            return function(request, *args, **kwargs)
        else:
            logging.error(request, 'You do not have permission for this action!')
            messages.error(request, _('You do not have permission for this action!'))
            return redirect('container-list')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
