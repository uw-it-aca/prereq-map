from django.urls import re_path
from prereq_map.views import PageView, CurricApiView, CourseApiView

urlpatterns = [
    re_path(r'^api/curric/(?P<curric_code>.*)', CurricApiView.as_view()),
    re_path(r'^api/course/(?P<course_code>.*)', CourseApiView.as_view()),
    re_path(r'.*', PageView.as_view())
]
