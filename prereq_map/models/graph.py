# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class CourseGraphCache(ExportModelOperationsMixin('CourseGraph'), models.Model):
    course_id = models.CharField(max_length=12, unique=True)
    needs_rebuild = models.BooleanField(default=False)
    graph_data = models.TextField()


class CurricGraphCache(ExportModelOperationsMixin('CurricGraph'), models.Model):
    curric_id = models.CharField(max_length=12, unique=True)
    needs_rebuild = models.BooleanField(default=False)
    graph_data = models.TextField()
