from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^select/(?P<project_id>\d+)/(?P<user_id>\d+)$', views.project_select, name='project-select'),
    url(r'^create', views.create_project, name='create-project'),
]