from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='container-index'),
    url(r'^list$', views.container_list, name='container-list'),
]