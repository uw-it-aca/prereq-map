import json

from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.views import View
from prereq_map.utils.process_data import get_graph
from prereq_map.utils.typeahead import get_curric_typeahead


class CurricApiView(View):
    @cache_control(max_age=86400)
    def get(self, request, curric_code):
        response = get_graph(curric_filter=curric_code.upper())
        if len(response['x']['nodes']['course_number']) > 0:
            return HttpResponse(json.dumps(response))
        else:
            return error_404()


class CourseApiView(View):
    @cache_control(max_age=86400)
    def get(self, request, course_code):
        response = get_graph(course_filter=course_code.upper())
        if response:
            return HttpResponse(json.dumps(response))
        else:
            return error_404()


class CurricTypeaheadApiView(View):
    @cache_control(max_age=86400)
    def get(self, request):
        response = get_curric_typeahead()
        return HttpResponse(json.dumps(response))


def error_404():
    response = HttpResponse()
    response.status_code = 404
    return response
