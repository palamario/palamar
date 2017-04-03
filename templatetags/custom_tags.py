from dateutil.parser import parse
import datetime
import pytz

from oslo_i18n import translate as _

from django.template import library
from django.conf import settings

register = library.Library()


@register.filter(expects_localtime=True)
def parse_iso(value):
    return parse(value)


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
        readable_format = _('%s %s, %s %s' % (td.days,day,td.seconds // 3600,hour))
    return readable_format

@register.assignment_tag()
def return_sites(Sites):
    from sites.models import Sites
    sites = Sites.objects.all()
    return sites