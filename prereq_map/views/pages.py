from django.views.generic import TemplateView
from uw_sws.term import get_current_term


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
        response = super(CurriculumSearch, self).render_to_response(
            context, **response_kwargs)

        # get the current term
        print("term resource...")
        term = get_current_term()
        print(term)
        # get the last final exam date for given term
        #print(term.last_final_exam_date)

        # check to see if the onboarding cookie exists, if not create it
        if 'onboarding-accepted' not in self.request.COOKIES:
            # set cookie to expire in 30 sec
            # TODO: Change to Term API last day of finals week
            response.set_cookie("onboarding-accepted", "false", max_age=30)

        return response


class CourseSearch(TemplateView):
    template_name = "course-search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
