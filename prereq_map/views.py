from django.views.generic import TemplateView, View
from django.http import HttpResponse
from prereq_map.utils.process_data import process_data
import json


class PageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ApiView(View):
    def get(self, request, curric_code):
        response = process_data(curric_code.upper())
        return HttpResponse(json.dumps(response))


