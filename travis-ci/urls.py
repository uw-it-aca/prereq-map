from django.urls import path, include
urlpatterns = [
    path(r'^', include('prereq_map.urls'))
]