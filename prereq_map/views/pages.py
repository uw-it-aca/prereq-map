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

    def render_to_response(self, context, **response_kwargs):
        response = super(CurriculumSearch, self).render_to_response(context, **response_kwargs)

        if not self.request.COOKIES.get('onboarding-accepted'):
            # set cookie to expire in 1 minute (60 sec.)
            response.set_cookie("onboarding-accepted","false", 60)
        return response


class CourseSearch(TemplateView):
    template_name = "course-search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
