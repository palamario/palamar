from django.contrib import admin

from .models import Role,Assignment

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    pass

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'role','type', 'actor', 'target_domain', 'target_project')
    list_filter = ('type', 'actor', 'role')
    pass

admin.site.register(Role, RoleAdmin)
admin.site.register(Assignment, AssignmentAdmin)