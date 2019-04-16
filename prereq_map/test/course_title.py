from django.test import TestCase
from prereq_map.models.course_title import CourseTitle
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
