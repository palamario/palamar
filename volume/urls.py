from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.volume_list, name='volume-index'),
    url(r'^$', views.volume_list, name='volume-list'),
]
