from drf_tz_fields.utils import normalize_tz_name
import pytz
from django.utils import six
from rest_framework.serializers import Field, ValidationError
from timezone_field.utils import is_pytz_instance
from django.utils.translation import ugettext_lazy as _t

__author__ = 'slessans'

class TimeZoneField(Field):

    default_error_messages = {
        'unknown_tz': _t('not a valid timezone name.')
    }

    def __init__(self, strict=True, **kwargs):
        super().__init__(**kwargs)
        self.strict = strict

    def to_representation(self, value):
        if value is None or value == '':
            return None
        if is_pytz_instance(value):
            return value.zone
        raise ValidationError("Invalid timezone value '%s'" % value)

    def to_internal_value(self, value):
        if is_pytz_instance(value):
            return value

        if isinstance(value, six.string_types):
            if not self.strict:
                value = normalize_tz_name(value)
            try:
                return pytz.timezone(value)
            except pytz.UnknownTimeZoneError:
                pass

        self.fail('unknown_tz')
