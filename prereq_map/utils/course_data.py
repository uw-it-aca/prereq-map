from uw_sws.course import get_course_by_label
from uw_sws.term import get_current_term
from restclients_core.exceptions import DataFailureException


def get_course_details(course_id):
    term = get_current_term()
    try:
        course = get_course_for_term(course_id, term)
    except DataFailureException:
        pass
    return course


def get_course_for_term(course_id, term):
    label = get_course_label(term, course_id)
    import sys
    sys.stderr.write('Label:', label)
    course = get_course_by_label(label)
    sys.stderr.write('Course:', course)
    return course


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
    return label
