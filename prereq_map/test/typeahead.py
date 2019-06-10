from django.test import TestCase
from prereq_map.models.currics import CurricTitles
from prereq_map.utils.typeahead import get_curric_typeahead
import pandas as pd


class TestTypeahead(TestCase):
    def test_get_typeahead(self):
        CurricTitles.objects.create(abbrev='COM', name='Communications',
                                    campus=0)
        CurricTitles.objects.create(abbrev='CSE', name='Computer Science ',
                                    campus=1)

        typeahead = get_curric_typeahead()
        self.assertEqual(len(typeahead), 2)
        self.assertEqual(typeahead['Seattle: Communications (COM)'], "COM")

    def test_update_titles(self):
        typeahead = get_curric_typeahead()
        self.assertEqual(len(typeahead), 0)
        titles_dataframe = pd.DataFrame(
            {'curric_full_nm': ["COMPUTER SCIENCE AND EDUCATION",
                                "COMMUNICATION OF PEOPLE",
                                "GRADUATE CURRIC"],
             'curric_abbr': ['CSE', 'COM', 'GRAD'],
             'curric_branch': [0, 1, 2]
             }
        )
        course_dataframe = pd.DataFrame(
            {'course_number': [100, 344, 500],
             'department_abbrev': ['CSE', 'COM', 'GRAD']
             }
        )
        CurricTitles.update_titles(titles_dataframe, course_dataframe)
        typeahead = get_curric_typeahead()
        self.assertEqual(len(typeahead), 2)
        self.assertEqual(list(typeahead)[0],
                         "Seattle: Computer Science And Education (CSE)")
