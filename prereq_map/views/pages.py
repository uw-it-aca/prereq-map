from django.views.generic import TemplateView
from uw_sws.term import get_current_term
from restclients_core.exceptions import DataFailureException
import datetime


class PageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(PageView, self).render_to_response(
            context, **response_kwargs)
        try:
            # get the current term from the sws resource
            term = get_current_term()
            # set last_final_exam_date as the end of term date and format it
            term_end_date = term.last_final_exam_date
            # example format: Sat, 29 Mar 2019 12:25:57 GMT
            term_end_date = term_end_date.strftime("%c")
        except DataFailureException:
            term_end_date = datetime.datetime.now() + \
                            datetime.timedelta(days=7)
            term_end_date.strftime("%c")

        # check to see if the onboarding cookie exists
        if 'prereq-onboarding-accepted' not in self.request.COOKIES:
            # create/set accepted cookie value to false
            response.set_cookie("prereq-onboarding-accepted", "false")
            # create/set  term end date cookie and expire it in 1 week
            response.set_cookie("prereq-onboarding-expires", term_end_date)
        return response


class CurriculumSearch(TemplateView):
    template_name = "curriculum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(CurriculumSearch, self).render_to_response(
            context, **response_kwargs)
        try:
            # get the current term from the sws resource
            term = get_current_term()
            # set last_final_exam_date as the end of term date and format it
            term_end_date = term.last_final_exam_date
            # example format: Sat, 29 Mar 2019 12:25:57 GMT
            term_end_date = term_end_date.strftime("%c")
        except DataFailureException:
            term_end_date = datetime.datetime.now() + \
                            datetime.timedelta(days=7)
            term_end_date.strftime("%c")

        # check to see if the onboarding cookie exists
        if 'prereq-onboarding-accepted' not in self.request.COOKIES:
            # create/set accepted cookie value to false
            response.set_cookie("prereq-onboarding-accepted", "false")
            # create/set  term end date cookie and expire it in 1 week
            response.set_cookie("prereq-onboarding-expires", term_end_date)
        return response


class CourseSearch(TemplateView):
    template_name = "course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
