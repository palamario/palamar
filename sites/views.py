from oslo_i18n import translate as _

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from . models import Sites
from .forms import SiteEditForm

@login_required
def index(request):
    return render(request, "sites/index.html", {})

@login_required
def sites_list(request):
    title=_('List of Sites')
    subtitle=_('list all sites')
    breadcrumb=_('Sites')
    sites=Sites.objects.all()

    return render(request, "sites/sites_list.html", {"sites": sites,
                                                     "title": title,
                                                     "breadcrumb": breadcrumb,
                                                     "subtitle": subtitle,})

@login_required
def site_edit(request,pk):
    title=_('Edit Site')
    subtitle=_('update details of a site')
    breadcrumb=_('Edit Site')
    site = get_object_or_404(Sites, pk=pk)
    if request.method=='POST':
        form=SiteEditForm(request.POST,request.FILES)
        if form.is_valid():
            site.name=form.data['name']
            site.save()
            return redirect('sites_edit', pk=pk)
        else:
            print(form.errors)
    else:
        form=SiteEditForm()
    return render(request, "sites/site_edit.html", {
        "site": site,
        "title": title,
        "breadcrumb": breadcrumb,
        "subtitle": subtitle,
        "form": form,
        })