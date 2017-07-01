from dateutil.parser import parse
import datetime
import pytz

from oslo_i18n import translate as _
from cuser.middleware import CuserMiddleware

from django.template import library
from django.conf import settings

register = library.Library()

# Filters
@register.filter(expects_localtime=True)
def parse_iso(value):
    return parse(value)

@register.filter(expects_localtime=True)
def parse_timestamp(value):
    try:
        return datetime.datetime.fromtimestamp(value)
    except AttributeError as e:
        return e

@register.filter(expects_localtime=True)
def since_created(value):
    current_date = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    td = current_date - value
    if td.days > 1:
        day = "days"
    else:
        day = "day"

    if (td.seconds // 3600) > 1:
        hour = "hours"
    else:
        hour = "hour"

    if (td.seconds // 60) > 1:
        minute = "minutes"
    else:
        minute = "minute"

    if (td.seconds // 3600) < 1:
        readable_format = _('%s %s' % (td.seconds // 60, minute))
    elif td.days <= 0:
        readable_format = _('%s %s' % (td.seconds // 3600, hour))
    else:
        readable_format = _('%s %s, %s %s' % (td.days, day, td.seconds // 3600, hour))
    return readable_format

@register.filter()
def split_column(value):
    splitted_value = value.split(":")
    return splitted_value


# Tags
@register.assignment_tag()
def return_sites():
    from sites.models import Sites
    sites = Sites.objects.all()
    return sites

@register.assignment_tag()
def return_assigned_projects():
    current_user = CuserMiddleware.get_user()
    from user_profile.models import Profile
    from role.models import Assignment
    from django.db.models import Count
    current_user_profile = Profile.objects.get(user_id=current_user.id)
    projects = Assignment.objects.filter(type=1,
                                         actor=current_user.id,
                                         target_domain=current_user_profile.selected_domain)
    projects = projects.values('target_project_id', 'target_project__name')
    projects = projects.annotate(dcount=Count('target_project_id'))
    return projects

@register.assignment_tag()
def return_assigned_domains():
    current_user = CuserMiddleware.get_user()
    from role.models import Assignment
    from django.db.models import Count
    assigned_domains = Assignment.objects.filter(type=3, actor=current_user.id)
    assigned_domains = assigned_domains.values('target_domain_id', 'target_domain__name')
    assigned_domains = assigned_domains.annotate(dcount=Count('target_domain_id'))
    return assigned_domains

