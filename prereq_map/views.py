from django.views.generic import TemplateView, View
from django.http import HttpResponse
from prereq_map.utils.process_data import process_data


class PageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('prereq_map/data/chem_map.json', 'r') as myfile:
            graph_data = myfile.read().replace('\n', '')
        # context['json_data'] = graph_data
        context['json_data'] = process_data("CSE")
        return context


class ApiView(View):
    def get(self, request):
        with open('prereq_map/data/chem_map.json', 'r') as myfile:
            graph_data = myfile.read().replace('\n', '')

        return HttpResponse(graph_data)

