# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.core.management.base import BaseCommand
from prereq_map.models.graph import CourseGraphCache, CurricGraphCache
from prereq_map.models.course_title import CourseTitle
from prereq_map.models.currics import CurricTitles


class Command(BaseCommand):
    def handle(self, *args, **options):
        CourseGraphCache.objects.all().delete()
        CurricGraphCache.objects.all().delete()
        CourseTitle.objects.all().delete()
        CurricTitles.objects.all().delete()
