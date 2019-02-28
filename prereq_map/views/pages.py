from django.views.generic import TemplateView


class PageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CurriculumSearch(TemplateView):
    template_name = "curriculum-search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseSearch(TemplateView):
    template_name = "course-search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
