from django.db import models


class CourseTitle(models.Model):
    department_abbrev = models.CharField(max_length=6)
    course_number = models.SmallIntegerField()
    last_eff_yr = models.SmallIntegerField()
    last_eff_qtr = models.SmallIntegerField()
    course_branch = models.SmallIntegerField()
    course_college = models.CharField(max_length=1)
    long_course_title = models.CharField(max_length=120)
    prq_lang_of_adm = models.SmallIntegerField()
    prq_check_grads = models.CharField(max_length=1)
    pre_cancel_req = models.CharField(max_length=1)
    course_cat_omit = models.BooleanField()
    writing_crs = models.BooleanField()
    diversity_crs = models.BooleanField()
    english_comp = models.BooleanField()
    qsr = models.BooleanField()
    vis_lit_perf_arts = models.BooleanField()
    indiv_society = models.BooleanField()
    natural_world = models.BooleanField()
