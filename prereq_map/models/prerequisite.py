from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Prerequisite(ExportModelOperationsMixin('Prerequisite'), models.Model):
    course_branch = models.SmallIntegerField()
    department_abbrev = models.CharField(max_length=32)
    course_number = models.SmallIntegerField()
    last_eff_year = models.SmallIntegerField()
    last_eff_qtr = models.CharField(max_length=6)
    pr_seq_no = models.SmallIntegerField()
    pr_curric_abbr = models.CharField(max_length=32)
    pr_course_no = models.SmallIntegerField()
    pr_group_no = models.SmallIntegerField()
    pr_and_or = models.CharField(max_length=3)
    pr_cr_s = models.BooleanField()
    pr_concurrency = models.BooleanField()
