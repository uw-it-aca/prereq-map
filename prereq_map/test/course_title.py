from django.test import TestCase
from prereq_map.models.course_title import CourseTitle
from prereq_map.utils.typeahead import get_course_typeahead
import pandas as pd


class TestCourseTitle(TestCase):
    def test_titles(self):
        dataframe = pd.DataFrame(
            {'department_abbrev': ['CSE', 'LAW'],
             'course_number': [142, 354],
             'course_college': ['School of Arts and Sci', 'Law School'],
             'long_course_title': ['Intro To Java', 'Bird Law']
             }
        )
        CourseTitle.update_titles(dataframe)
        self.assertEqual(len(CourseTitle.objects.all()), 2)

        title = CourseTitle().get_course_title("CSE 142")
        self.assertEqual(title, "Intro To Java")
        with self.assertRaises(CourseTitle.DoesNotExist):
            CourseTitle.get_course_title("CSE 500")

    def test_typeahead(self):
        CourseTitle(department_abbrev="CSE",
                    course_number="142",
                    long_course_title="Intro to Comp Sci").save()
        CourseTitle(department_abbrev="MATH",
                    course_number="123",
                    long_course_title="Counting by Numbers").save()
        ct_typeahead = get_course_typeahead()
        self.assertEqual(len(ct_typeahead), 2)
        self.assertEqual(ct_typeahead[0], "CSE 142: Intro to Comp Sci")
