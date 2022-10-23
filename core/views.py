from core.serializers import ScreenSerializer
from core.models import Screen
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ScreenList(ListAPIView):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer


class ScreenRetrieve(RetrieveAPIView):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
