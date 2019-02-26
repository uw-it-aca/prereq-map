from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from prereq_map.views import PageView, CurricApiView, CourseApiView, CurriculumSearch, CourseSearch

urlpatterns = [
    path('', RedirectView.as_view(url='/curriculum-search/')),
    path('curriculum-search/', CurriculumSearch.as_view()),
    path('course-search/', CourseSearch.as_view()),
    re_path('api/course/(?P<course_code>.*)', CourseApiView.as_view()),
    re_path('api/curric/(?P<curric_code>.*)', CurricApiView.as_view())
]
