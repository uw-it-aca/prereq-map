# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.core.management.base import BaseCommand
from prereq_map.utils.build_graphs import rebuild_graphs


class Command(BaseCommand):
    def handle(self, *args, **options):
        rebuild_graphs()
