from django.test import TestCase, Client
from prereq_map.utils.course_data import get_section_details,\
    split_course, get_course_label
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
                         "2013,spring,CSE,142/A")

    def test_get_section(self):
        section = get_section_details("CSE 142")
        self.assertIsNotNone(section)
