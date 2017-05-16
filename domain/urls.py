from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^select/(?P<domain_id>\d+)/(?P<user_id>\d+)$', views.domain_select, name='domain-select'),
]