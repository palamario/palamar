from django.contrib import admin

from project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domain', 'enabled')
    pass

admin.site.register(Project, ProjectAdmin)
