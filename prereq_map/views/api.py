# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json

from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.views import View
from prereq_map.utils.process_data import get_graph
from prereq_map.utils.typeahead import get_curric_typeahead
from prereq_map.utils.typeahead import get_course_typeahead
import logging

logger = logging.getLogger(__name__)


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
        logger.info('Get course graph for: %s' % course_code.upper())
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


class CourseTypeaheadApiView(View):
    @cache_control(max_age=86400)
    def get(self, request):
        response = get_course_typeahead()
        return HttpResponse(json.dumps(response))


def error_404():
    response = HttpResponse()
    response.status_code = 404
    return response
