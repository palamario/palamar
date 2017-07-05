import datetime
import json
from oslo_i18n import translate as _

from cuser.middleware import CuserMiddleware
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages


from palamar.drivers.docker_api import ConnectDocker


@login_required
def index(request):
    return render(request, "container/index.html", {})


@login_required
def container_create(request):
    title = _("Create Container")
    subtitle = _("create a new container")
    user_profile = request.user.profile
    current_user = CuserMiddleware.get_user()
    conn = ConnectDocker(user_profile.selected_site)
    client = conn.docker_connect()
    # define variables
    image = 'alpine'
    command = None
    auto_remove = False
    blkio_weight_device = None
    blkio_weight = None
    cap_add = None
    cap_drop = None
    hostname = None
    cpu_count = None
    cpu_percent = None
    cpu_period = None
    cpu_quota = None
    cpu_shares = None
    cpuset_cpus = None
    cpuset_mems = None
    detach = False
    device_read_bps = None
    device_read_iops = None
    device_write_bps = None
    device_write_iops = None
    devices = None
    dns = None
    dns_ops = None
    dns_search = None
    domainname = None
    entrypoint = None
    environment = None
    extra_hosts = None
    group_add = None
    hostname = None
    init = None
    init_path = None
    ipc_mode = None
    isolation = None
    labels = {
              "site_id": str(user_profile.selected_site),
              "domain_id": str(user_profile.selected_domain),
              "project_id": str(user_profile.selected_project),
              "user_id": str(current_user.id)
              }
    #labels = ["site_id", "domain_id"]
    links = {}
    log_config = []
    mac_address = None
    mem_limit = None
    mem_swappiness = 100
    memswap_limit = None
    name = ""
    nano_cpus = 1
    network = ""
    network_disabled = False
    network_mode = "bridge"
    oom_kill_disable = False
    oom_score_adj = None
    pid_mode = None
    pids_limit = 200
    ports = {}
    privileged = False
    publish_all_ports = False
    read_only = False
    remove = False
    restart_policy = {}
    security_opt = []
    shm_size = None
    stdin_open = False
    stdout = True
    stderr = False
    stop_signal = "SIGINT"
    storage_opt = {}
    sysctls = {}
    tmpfs = {}
    tty = False
    ulimits = {}
    user = ""
    userns_mode = ""
    volume_driver = ""
    volumes = {}
    volumes_from = None
    working_dir = None

    container = client.containers.run(image,
                                      command,
                                      detach=True,
                                      labels=labels,)

    return render(request, "container/container_create.html", {"title": title,
                                                               "subtitle": subtitle,
                                                               "container": container,})

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