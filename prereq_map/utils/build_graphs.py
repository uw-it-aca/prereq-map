import threading
import os
import json
import pandas as pd
from prereq_map.utils.process_data import process_data
from prereq_map.models.graph import CourseGraph, CurricGraph


def build_graphs():
    curric_list = get_currics()
    curric_graphs = []
    for curric in curric_list:
        graph_json = json.dumps(process_data(curric_filter=curric.strip()))
        curric_graphs.append(CurricGraph(curric_id=curric,
                                         graph_data=graph_json))
    CurricGraph.objects.all().delete()
    CurricGraph.objects.bulk_create(curric_graphs)

    course_list = get_courses()
    course_graphs = []
    for course in course_list:
        graph_json = json.dumps(process_data(course_filter=course))
        course_graphs.append(CourseGraph(course_id=course,
                                         graph_data=graph_json))
    CourseGraph.objects.all().delete()
    CourseGraph.objects.bulk_create(course_graphs)


def get_currics():
    currics = []
    course_data = _get_course_data()
    currics = course_data['department_abbrev'].unique()
    return currics


def get_courses():
    courses = []
    course_data = _get_course_data()
    course_data['course'] = (course_data['department_abbrev'] +
                             " " + course_data['course_number'].map(str))
    courses = course_data['course']
    return courses


def _get_course_data():
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')
    return pd.read_pickle(os.path.join(data_path, "course_data.pkl"))
