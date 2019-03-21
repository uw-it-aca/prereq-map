from django.conf import settings
import re
from uw_sws.section import get_section_by_label
from uw_sws.term import get_term_before, get_term_after, get_current_term
from restclients_core.exceptions import DataFailureException

FUTURE_TERMS_SEARCH_DEFAULT = 2
PRIOR_TERMS_SEARCH_DEFAULT = 3


def get_section_details(course_label):
    section_labels = []
    curric, course = split_course(course_label)

    for section_label in section_labels:
        try:
            section = get_section_by_label(section_label)
            return section
        except DataFailureException:
            pass


def split_course(course_label):
    parts = course_label.split()
    curric = " ".join(parts[:-1])
    return curric, parts[-1]


def get_course_label(year, quarter, curric, course):
    return ",".join([str(year), quarter, curric, course])


def get_prior_terms(term):
    terms = []
    prior_terms = getattr(settings, "PRIOR_TERMS_SEARCH",
                          PRIOR_TERMS_SEARCH_DEFAULT)
    for i in range(prior_terms):
        try:
            term = get_term_before(term)
            terms.insert(0, term)
        except DataFailureException as ex:
            if ex.status == 404:
                pass

    return terms


def get_future_terms(term):
    terms = []
    future_terms = getattr(settings, "FUTURE_TERMS_SEARCH",
                           FUTURE_TERMS_SEARCH_DEFAULT)
    for i in range(future_terms):
        try:
            term = get_term_after(term)
            terms.append(term)
        except DataFailureException as ex:
            if ex.status == 404:
                pass

    return terms
