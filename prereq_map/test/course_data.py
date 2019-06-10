from django.test import TestCase, Client
from prereq_map.utils.course_data import split_course, get_course_label, \
    get_course_details
from uw_sws.term import get_term_by_year_and_quarter


class TestCourse(TestCase):
    def test_split_course(self):
        course = "CSE 142"
        self.assertEqual(split_course(course), ("CSE", "142"))
        course = "B BIO 123"
        self.assertEqual(split_course(course), ("B BIO", "123"))

    def test_course_label(self):
        term = get_term_by_year_and_quarter(2013, 'spring')
        self.assertEqual(get_course_label(term, "CSE 142"),
                         "2013,spring,CSE,142")

    def test_get_course(self):
        section = get_course_details("CSE 142")
        self.assertIsNotNone(section)
        desc = "Basic programming-in-the-small abilities and concepts" \
               " including procedural programming (methods, parameters, " \
               "return, values), basic control structures (sequence, " \
               "if/else, for loop, while loop), file processing, arrays," \
               " and an introduction to defining objects. Intended for " \
               "students without prior programming experience. Offered: AWSpS."
        self.assertEqual(section.course_description, desc)
