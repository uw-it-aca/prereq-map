from django.test import TestCase, Client
from prereq_map.utils.course_data import get_section_details, split_course, get_course_label


class TestCourse(TestCase):
    def test_split_course(self):
        course = "CSE 142"
        self.assertEqual(split_course(course), ("CSE", "142"))
        course = "B BIO 123"
        self.assertEqual(split_course(course), ("B BIO", "123"))

    def test_course_label(self):
        self.assertEqual(get_course_label(2019, "winter", "CSE", "142"),
                         "2019,winter,CSE,142")

