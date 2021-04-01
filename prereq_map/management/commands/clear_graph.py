# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.core.management.base import BaseCommand
from prereq_map.models.graph import CourseGraph, CurricGraph


class Command(BaseCommand):
    def handle(self, *args, **options):
        CourseGraph.objects.all().delete()
        CurricGraph.objects.all().delete()
