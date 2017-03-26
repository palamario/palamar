from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from user_profile.models import Profile
from sites.models import Sites


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


class SitesInline(admin.StackedInline):
    model = Sites
    can_delete = False
    verbose_name_plural = 'sites'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
