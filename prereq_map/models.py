from django.db import models


class Prerequisite(models.Model):
    course_branch = models.SmallIntegerField()
    department_abbrev = models.CharField()
    course_number = models.SmallIntegerField()
    last_eff_year = models.SmallIntegerField()
    last_eff_qtr = models.CharField()
    pr_seq_no = models.SmallIntegerField()
    pr_curric_abbr = models.CharField()
    pr_course_no = models.SmallIntegerField()
    pr_group_no = models.SmallIntegerField()
    pr_and_or = models.CharField()
    pr_cr_s = models.BooleanField()
    pr_concurrency = models.BooleanField()
