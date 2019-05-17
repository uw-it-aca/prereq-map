import threading
import os
import json
import pandas as pd
import re
from prereq_map.utils.process_data import _process_data, get_prereq_data, \
    get_course_data, process_data
from prereq_map.models.graph import CourseGraph, CurricGraph

# Number of graphs to bulk_create at once
GRAPH_SAVE_LIMIT = 1000


def rebuild_graphs():
    # to rebuild ALL graphs should be set higher than total UW course count
    graphs_to_build = 900000
    reset_course_graphs()
    build_curric_graphs()
    build_course_graphs(graphs_to_build)


def reset_course_graphs():
    CourseGraph.objects.all().update(needs_rebuild=True)


def build_curric_graphs():
    curric_list = get_currics()
    curric_graphs = []
    for curric in curric_list:
        graph_json = json.dumps(process_data(curric_filter=curric.strip()))
        curric_graphs.append(CurricGraph(curric_id=curric,
                                         graph_data=graph_json))
    CurricGraph.objects.all().delete()
    CurricGraph.objects.bulk_create(curric_graphs)


def build_course_graphs(count):
    # Update existing course models
    courses = get_courses()
    course_obj_to_update = CourseGraph.objects.filter(course_id__in=courses,
                                                      needs_rebuild=True)
    courses_saved = 0
    course_data = get_course_data()
    prereq_data = get_prereq_data()
    for course_obj in course_obj_to_update[:count]:
        graph_json = json.dumps(_process_data(
            course_data,
            prereq_data,
            course_filter=course_obj.course_id
        ))
        course_obj.graph_data = graph_json
        course_obj.needs_rebuild = False
        course_obj.save()
        courses_saved += 1

    if courses_saved < count:
        # Add courses w/o model
        existing_courses = CourseGraph.objects.all().values_list('course_id',
                                                                 flat=True)
        new_courses = list(set(courses) - set(existing_courses))
        new_graphs = []

        for course in new_courses[:count - courses_saved]:
            course = re.sub(' +', ' ', course)
            graph_json = json.dumps(_process_data(
                course_data,
                prereq_data,
                course_filter=course
            ))
            new_graphs.append(CourseGraph(course_id=course,
                                          graph_data=graph_json))
            if len(new_graphs) == GRAPH_SAVE_LIMIT:
                CourseGraph.objects.bulk_create(new_graphs)
                new_graphs.clear()
        CourseGraph.objects.bulk_create(new_graphs)


def get_currics():
    currics = []
    course_data = _get_course_data()
    currics = course_data['department_abbrev'].unique()
    return currics.tolist()


def get_courses():
    courses = []
    course_data = _get_course_data()
    course_data['course'] = (course_data['department_abbrev'] +
                             " " + course_data['course_number'].map(str))
    courses = course_data['course']
    return courses.tolist()


def _get_course_data():
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')
    return pd.read_pickle(os.path.join(data_path, "course_data.pkl"))
