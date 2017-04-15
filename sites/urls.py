from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='sites-index'),
    url(r'^list/$', views.sites_list, name='sites-list'),
    url(r'^create/$', views.site_create, name='site-create'),
    url(r'^edit/(?P<pk>\d+)$', views.site_edit, name='site-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.site_delete, name='site-delete'),
    url(r'^select/(?P<site_id>\d+)/(?P<user_id>\d+)$', views.site_select, name='site-select'),
]