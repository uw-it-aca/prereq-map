from django.urls import re_path, include
urlpatterns = [
    re_path(r'^', include('django_prometheus.urls')),
    re_path(r'^', include('prereq_map.urls')),
]
