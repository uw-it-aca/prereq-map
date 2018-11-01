from django.urls import re_path
from prereq_map.views import PageView

urlpatterns = [
    re_path(r'.*', PageView.as_view()),
]
