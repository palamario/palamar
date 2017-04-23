from django.contrib import admin

from .models import Quotas,Classes, Usages, Reservations, Resources

class QuotasAdmin(admin.ModelAdmin):
    pass


class ClassesAdmin(admin.ModelAdmin):
    pass


class UsagesAdmin(admin.ModelAdmin):
    pass


class ReservationsAdmin(admin.ModelAdmin):
    pass


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

admin.site.register(Quotas,QuotasAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Usages, UsagesAdmin)
admin.site.register(Reservations, ReservationsAdmin)
admin.site.register(Resources, ResourcesAdmin)

