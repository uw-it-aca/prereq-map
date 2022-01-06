# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from prereq_map.models.currics import CurricTitles
from prereq_map.models.course_title import CourseTitle


def get_curric_typeahead():
    currics = CurricTitles.objects.all()
    curric_data = {}
    for curric in currics:
        curric_data.update(curric.get_display_data())
    return curric_data


def get_course_typeahead():
    courses = CourseTitle.objects.all()
    course_data = []
    for course in courses:
        course_data.append(course.json_data())
    return course_data
