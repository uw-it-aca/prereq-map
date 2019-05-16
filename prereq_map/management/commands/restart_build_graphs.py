from django.core.management.base import BaseCommand
from prereq_map.utils.build_graphs import build_course_graphs, \
    build_curric_graphs


class Command(BaseCommand):
    def handle(self, *args, **options):
        build_curric_graphs()
        build_course_graphs(900000)
