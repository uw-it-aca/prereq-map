from django.core.management.base import BaseCommand
from prereq_map.models.graph import CourseGraph, CurricGraph


class Command(BaseCommand):
    def handle(self, *args, **options):
        CourseGraph.objects.all().delete()
        CurricGraph.objects.all().delete()
