from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.image_list, name='image-index'),
    url(r'^$', views.image_list, name='image-list'),
]
