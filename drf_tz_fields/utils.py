__author__ = 'slessans'

_NORMALIZED_TZ_MAP = None

def _get_normalized_tz_map():
    global _NORMALIZED_TZ_MAP
    if _NORMALIZED_TZ_MAP is None:
        from pytz import all_timezones
        _NORMALIZED_TZ_MAP = {tz_name.lower(): tz_name for tz_name in all_timezones}
    return _NORMALIZED_TZ_MAP

def normalize_tz_name(value: str) -> str:
    value = value.strip().lower()
    value = value.replace(' ', '_')

    tz_map = _get_normalized_tz_map()
    if value in tz_map:
        return tz_map[value]
    return value
