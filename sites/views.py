from oslo_i18n import translate as _

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user_profile.models import Profile

from . models import Sites
from .forms import SiteCreateForm,SiteEditForm


@login_required
def index(request):
    return render(request, "sites/index.html", {})


@login_required
def site_create(request):
    title = _('New Site')
    subtitle = _('create new site')
    if request.method=='POST':
        form=SiteCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            site=Sites(
                name=form.cleaned_data['name'],
                url=form.cleaned_data['url'],
                client_cert=form.cleaned_data['client_cert'],
                client_key=form.cleaned_data['client_key'],
                ca_cert=form.cleaned_data['ca_cert'],
                ssl_verify=form.cleaned_data['ssl_verify'],
            )
            site.save()
            messages.success(request,_('New site has been created!'))
            return redirect('sites-list')
        else:
            print(form.errors)
    else:
        form=SiteCreateForm()
    return render(request, "sites/site_create.html", {
        "title": title,
        "subtitle": subtitle,
        "form": form,
        })


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
    site=get_object_or_404(Sites, pk=pk)
    if request.method=='POST':
        form=SiteEditForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            site.name=form.cleaned_data['name']
            site.url=form.cleaned_data['url']
            if form.cleaned_data['client_cert']:
                site.client_cert.delete()
                site.client_cert=form.cleaned_data['client_cert']
            if form.cleaned_data['client_key']:
                site.client_key.delete()
                site.client_key=form.cleaned_data['client_key']
            if form.cleaned_data['ca_cert']:
                site.ca_cert.delete()
                site.ca_cert=form.cleaned_data['ca_cert']
            site.ssl_verify=form.cleaned_data['ssl_verify']
            site.save()
            messages.success(request, _('Site updated!'))
            return redirect("sites-list")
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


@login_required
def site_delete(request,pk):
    site=get_object_or_404(Sites,pk=pk)
    site.delete()
    messages.success(request, _('Site deleted!'))
    return redirect("sites-list")


@login_required
def site_select(request,site_id,user_id):
    user = get_object_or_404(Profile, pk=user_id)
    user.selected_site = site_id
    user.save()
    return redirect(request.META['HTTP_REFERER'])