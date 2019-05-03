import json

from django.http import HttpResponse
from django.views import View
from prereq_map.utils.process_data import get_graph
from prereq_map.utils.typeahead import get_curric_typeahead


class CurricApiView(View):
    def get(self, request, curric_code):
        response = get_graph(curric_filter=curric_code.upper())
        return HttpResponse(json.dumps(response))


class CourseApiView(View):
    def get(self, request, course_code):
        response = get_graph(course_filter=course_code.upper())
        return HttpResponse(json.dumps(response))


class CurricTypeaheadApiView(View):
    def get(self, request):
        response = get_curric_typeahead()
        return HttpResponse(json.dumps(response))
