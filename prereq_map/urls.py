from django.urls import re_path
from prereq_map.views import PageView, ApiView

urlpatterns = [
    re_path(r'^api/', ApiView.as_view()),
    re_path(r'.*', PageView.as_view())
]
