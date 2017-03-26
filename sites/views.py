from oslo_i18n import translate as _

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

from . models import Sites

@login_required
def index(request):
    return render(request, "sites/index.html", {})

@login_required
def sites_list(request):
    title=_('List of Sites')
    subtitle=_('list all sites')
    breadcrumb="Sites"
    sites=Sites.objects.all()


    return render(request, "sites/list_sites.html", {"sites": sites,
                                                     "title": title,
                                                     "breadcrumb": breadcrumb,
                                                     "subtitle": subtitle,})
