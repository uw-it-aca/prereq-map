from django.db import models


class CourseGraph(models.Model):
    course_id = models.CharField(max_length=12, primary_key=True)
    needs_rebuild = models.BooleanField(default=False)
    graph_data = models.TextField()


class CurricGraph(models.Model):
    curric_id = models.CharField(max_length=12, primary_key=True)
    needs_rebuild = models.BooleanField(default=False)
    graph_data = models.TextField()
