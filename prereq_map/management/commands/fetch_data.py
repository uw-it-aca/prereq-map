from django.core.management.base import BaseCommand, CommandError
import os
import pyodbc
import pandas
from django.conf import settings
from prereq_map.models.currics import CurricTitles
from prereq_map.models.course_title import CourseTitle


class Command(BaseCommand):
    def handle(self, *args, **options):
        password = getattr(settings, "EDW_PASSWORD")
        user = getattr(settings, "EDW_USER")
        data_root = getattr(settings, "DATA_ROOT")
        constring = "Driver={FreeTDS};" \
                    "Server=edwpub.s.uw.edu;" \
                    "Database=UWSDBDataStore;" \
                    "Port=1433;" \
                    "TDS_Version=7.2;" \
                    f"UID={user};" \
                    f"PWD={password}"
        con = pyodbc.connect(constring)

        prereq = pandas.read_sql(
            'select * from sec.sr_course_prereq where last_eff_yr = 9999', con)
        course_info = pandas.read_sql(
            'select * from sec.sr_course_titles where last_eff_yr = 9999', con)
        curric_info = pandas.read_sql("select * from sec.sr_curric_code where "
                                      "curric_last_yr = 9999", con)
        con.close()
        CurricTitles.update_titles(curric_info)
        CourseTitle.update_titles(course_info)

        prereq.to_pickle(os.path.join(data_root, "prereq_data.pkl"))
        course_info.to_pickle(os.path.join(data_root, "course_data.pkl"))
        curric_info.to_pickle(os.path.join(data_root, "curric_data.pkl"))
