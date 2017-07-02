from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.network_list, name='network-index'),
    url(r'^$', views.network_list, name='network-list'),
]
