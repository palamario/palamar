import docker

from sites.models import Sites
from django.shortcuts import get_object_or_404
from django.conf import settings

file_storage_dir = settings.FILE_STORAGE

class ConnectDocker(object):

    def __init__(self, selected_site, **kwargs):
        self.selected_site = selected_site

    def docker_connect(self):
        site=get_object_or_404(Sites, pk=self.selected_site)

        tls_config = docker.tls.TLSConfig(
            client_cert=(
                "%s/%s" % (file_storage_dir,site.client_cert),
                "%s/%s" % (file_storage_dir,site.client_key),
                ),
            ca_cert = "%s/%s" % (file_storage_dir,site.ca_cert),
            verify=site.ssl_verify
        )
        client = docker.DockerClient(base_url=site.url, tls=tls_config)
        return client