import pytz
from timezone_field import TimeZoneField as BaseTimeZoneField

__author__ = 'slessans'

class TimeZoneField(BaseTimeZoneField):
    """
    Just like time zone fields except uses pytz.all_timezones as possible choices rather than
    just pytz.common_timezone
    """
    CHOICES = [(tz, tz) for tz in pytz.all_timezones]
