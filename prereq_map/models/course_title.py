import re
from django.db import models


class CourseTitle(models.Model):
    department_abbrev = models.CharField(max_length=6)
    course_number = models.SmallIntegerField()
    course_college = models.CharField(max_length=1)
    long_course_title = models.CharField(max_length=120)

    @staticmethod
    def update_titles(titles_dataframe):
        CourseTitle.objects.all().delete()
        title_objects = []
        for idx, row in titles_dataframe.iterrows():
            title_objects.append(
                CourseTitle(
                    department_abbrev=row['department_abbrev'].strip(),
                    course_number=row['course_number'],
                    course_college=row['course_college'],
                    long_course_title=row['long_course_title']
                )
            )
        CourseTitle.objects.bulk_create(title_objects)

    @staticmethod
    def get_course_title(course_filter):
        regex = re.compile(r'^([a-zA-Z\s]+)(\d+)')
        match = regex.match(course_filter)
        try:
            dept_abbr = match.group(1).strip()
            course_num = match.group(2)
            course = CourseTitle.objects.get(department_abbrev=dept_abbr,
                                             course_number=course_num)
            return course.long_course_title
        except AttributeError:
            return ""

    def json_data(self):
        # remove extra whitespace from long_course_title
        self.long_course_title = " ".join(
            self.long_course_title.split()).rstrip()
        return ("%s %s: %s" % (self.department_abbrev,
                               self.course_number,
                               self.long_course_title))
