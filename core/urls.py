from django.urls import re_path
from core.views import ScreenList, ScreenRetrieve

urlpatterns = [
    re_path(r"^screens/(?P<pk>\d+)/?$", ScreenRetrieve.as_view(), name="screen-retrieve"),
    re_path(r"^screens/?$", ScreenList.as_view(), name="screens-list"),
]
