from django.test import TestCase
import pandas as pd
from prereq_map.utils.process_data import _process_data


class TestProcessData(TestCase):
    def test_process_curic(self):
        course_data = pd.DataFrame(
            {
                'department_abbrev': ['CSE', 'LAW', 'CSE'],
                'course_number': [142, 354, 143],
                'course_college': ['School of Arts and Sci', 'Law School',
                                   'School of Arts and Sci'],
                'long_course_title': ['Intro To Java', 'Bird Law',
                                      "Java II: More Coffee"],
            }
        )

        prereqs = pd.DataFrame(
            {
                'department_abbrev': ["CSE", "LAW"],
                'course_number': [143, 354],
                'pr_curric_abbr': ["CSE", "CSE"],
                'pr_course_no': ["142", "143"],
                'pr_and_or': ["", ""],
                "pr_concurrency": ["", ""],
                "pr_cr_s": ["", ""],
                "pr_grade_min": ["", ""],
                "pr_group_no": ["", ""],
                "pr_seq_no": ["", ""]
            }
        )

        pr_data = _process_data(course_data, prereqs, curric_filter="CSE")
        self.assertEqual(len(pr_data['x']['nodes']['course_number'].keys()), 2)
        self.assertEqual(pr_data['x']['edges']['from']['0'], "CSE 142")
        self.assertEqual(pr_data['x']['edges']['to']['0'], "CSE 143")

    def test_process_course(self):
        course_data = pd.DataFrame(
            {
                'department_abbrev': ['CSE', 'LAW', 'CSE'],
                'course_number': [142, 354, 143],
                'course_college': ['School of Arts and Sci', 'Law School',
                                   'School of Arts and Sci'],
                'long_course_title': ['Intro To Java', 'Bird Law',
                                      "Java II: More Coffee"],
            }
        )

        prereqs = pd.DataFrame(
            {
                'department_abbrev': ["CSE", "LAW"],
                'course_number': [143, 354],
                'pr_curric_abbr': ["CSE", "CSE"],
                'pr_course_no': ["142", "143"],
                'pr_and_or': ["", ""],
                "pr_concurrency": ["", ""],
                "pr_cr_s": ["", ""],
                "pr_grade_min": ["", ""],
                "pr_group_no": ["", ""],
                "pr_seq_no": ["", ""]
            }
        )

        pr_data = _process_data(course_data, prereqs, course_filter="CSE 143")
        self.assertEqual(len(pr_data['x']['nodes']['course_number'].keys()), 3)
        self.assertEqual(pr_data['x']['edges']['from']['0'], "CSE 142")
        self.assertEqual(pr_data['x']['edges']['to']['0'], "CSE 143")
        self.assertEqual(pr_data['x']['edges']['from']['1'], "CSE 143")
        self.assertEqual(pr_data['x']['edges']['to']['1'], "LAW 354")
