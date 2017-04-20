from django.contrib import admin

from .models import Domain

class DomainAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'enabled')
    list_filter = ('name', 'enabled')
    pass

admin.site.register(Domain, DomainAdmin)