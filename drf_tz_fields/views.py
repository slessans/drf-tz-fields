from rest_framework.response import Response
from rest_framework.views import APIView
from .fields import TimeZoneField

class TimeZoneView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return Response(data=[name for (name, _,) in TimeZoneField.CHOICES])

tz_view = TimeZoneView.as_view()
