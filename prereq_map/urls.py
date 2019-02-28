from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from prereq_map.views.pages import PageView, CurriculumSearch, CourseSearch
from prereq_map.views.api import CurricApiView, CourseApiView, \
    CurricTypeaheadApiView

urlpatterns = [
    path('', RedirectView.as_view(url='/curriculum-search/')),
    path('curriculum-search/', CurriculumSearch.as_view()),
    path('course-search/', CourseSearch.as_view()),
    re_path(r'^api/curric/(?P<curric_code>.*)', CurricApiView.as_view()),
    re_path(r'^api/course/(?P<course_code>.*)', CourseApiView.as_view()),
    re_path(r'^api/curric_typeahead', CurricTypeaheadApiView.as_view())
]
