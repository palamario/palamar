from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='container-index'),
    url(r'^create$', views.container_create, name='container-create'),
    url(r'^details/(?P<container_id>\w+)$', views.container_details, name='container-details'),
    url(r'^list$', views.container_list, name='container-list'),
    url(r'^stop/(?P<container_id>\w+)$', views.container_stop, name='container-stop'),
    url(r'^start/(?P<container_id>\w+)$', views.container_start, name='container-start'),
    url(r'^remove/(?P<container_id>\w+)$', views.container_remove, name='container-remove'),
]
