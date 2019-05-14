from django.conf import settings
import re
from uw_sws.section import get_section_by_label
from uw_sws.term import get_term_before, get_term_after, get_current_term
from restclients_core.exceptions import DataFailureException

FUTURE_TERMS_SEARCH_DEFAULT = 2
PRIOR_TERMS_SEARCH_DEFAULT = 3


def get_section_details(course_id):
    terms = get_search_terms()

    for term in terms:
        try:
            section = get_section_for_term(course_id, term)
            return section
        except DataFailureException:
            pass


def get_section_for_term(course_id, term):
    label = get_course_label(term, course_id)
    section = get_section_by_label(label)
    return section


def split_course(course_id):
    parts = course_id.split()
    curric = " ".join(parts[:-1])
    return curric, parts[-1]


def get_course_label(term, course):
    curric, course = split_course(course)
    # handle 2 digit courses
    if len(course) == 2:
        course = "0" + course

    label = ",".join([str(term.year), term.quarter, curric, course])
    # Assumes there is always an A section
    label += "/A"
    return label


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


def get_search_terms():
    terms = []
    current_term = get_current_term()
    terms.append(current_term)
    terms.extend(get_prior_terms(current_term))
    terms.extend(get_future_terms(current_term))
    return terms
