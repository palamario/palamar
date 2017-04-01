from dateutil.parser import parse
import datetime
import pytz

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
    if td.days <= 0:
        readable_format = '%s hour(s), %s minute(s) ' % (td.seconds // 3600,
                                                        (td.seconds // 60) % 60)
    else:
        readable_format = '%s day(s), %s hour(s), %s minute(s) ' % (td.days,
                                                                    td.seconds // 3600,
                                                                    (td.seconds // 60) % 60)
    return readable_format
