#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import pandas as pd
import os
import json
from prereq_map.models.course_title import CourseTitle
from prereq_map.utils.course_data import get_course_details
from prereq_map.models.graph import CourseGraphCache, CurricGraphCache
from uw_sws.exceptions import InvalidSectionID
from restclients_core.exceptions import DataFailureException
from django.conf import settings
from prometheus_client import Counter
import logging

"""
Unless we want to mess around with plots offline there should be no need to
use igraph or networkx. Unless we need to pre-define the coordinates for some
reason. Data can just be output from pandas DataFrame(s) to JSON.

Formatting - data should be divided between attributes of vertices/nodes and
attributes of the edges (e.g. concurrency, co-req). This should work for either
D3 or vis.js later on.

"data": {
        "nodes": {
                "id": [...]
                "name":[...]
                ...
                ...
        }
        "edges":{
                "from":[...]
                "to": [...]
                ...
                ...
        }
}
"""


logger = logging.getLogger(__name__)
CURRIC_BLACKLIST = ["TRAIN", "TTRAIN"]
USE_CACHE = getattr(settings, 'USE_CACHE', False)
CACHE_RESPONSES = Counter('graph_cache_responses', 'Responses cached')
UNCACHED_RESPONSES = Counter('graph_uncached_responses', 'Responses uncached')


def get_graph(curric_filter=None, course_filter=None):
    if curric_filter:
        try:
            if USE_CACHE:
                graph = CurricGraphCache.objects.get(curric_id=curric_filter)
                CACHE_RESPONSES.inc()
                return json.loads(graph.graph_data)
            else:
                return process_data(curric_filter=curric_filter)
        except CurricGraphCache.DoesNotExist:
            return process_data(curric_filter=curric_filter)
    if course_filter:
        try:
            if USE_CACHE:
                graph = CourseGraphCache.objects.get(course_id=course_filter)
                CACHE_RESPONSES.inc()
                return json.loads(graph.graph_data)
            else:
                return process_data(course_filter=course_filter)
        except CourseGraphCache.DoesNotExist:
            return process_data(course_filter=course_filter)


def process_data(curric_filter=None, course_filter=None):
    UNCACHED_RESPONSES.inc()
    course_data = get_course_data()
    prereqs = get_prereq_data()

    return _process_data(course_data, prereqs, curric_filter, course_filter)


def get_course_data():
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')
    # vertex attributes
    course_data = pd.read_pickle(os.path.join(data_path, "course_data.pkl"))
    # strip whitespace
    course_data = course_data.apply(
        lambda x: x.str.strip() if x.dtype == "object" else x)
    return course_data


def get_prereq_data():
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')
    # edgelist
    prereqs = pd.read_pickle(os.path.join(data_path, "prereq_data.pkl"))
    # strip whitespace
    prereqs = prereqs.apply(
        lambda x: x.str.strip() if x.dtype == "object" else x)
    return prereqs


def _process_data(course_data,
                  prereqs,
                  curric_filter=None,
                  course_filter=None):
    response = {}
    # create readable course from dept + #
    prereqs['course_to'] = prereqs['department_abbrev'] + " " + prereqs[
        'course_number'].map(str)
    prereqs['course_from'] = prereqs['pr_curric_abbr'] + " " + prereqs[
        'pr_course_no']
    pd.options.mode.chained_assignment = None
    course_data['course'] = (course_data['department_abbrev'] +
                             " " + course_data['course_number'].map(str))

    if curric_filter:
        course_data = course_data.loc[
            course_data['department_abbrev'] == curric_filter]
        prereqs = prereqs.loc[
            prereqs['department_abbrev'] == curric_filter]

    if course_filter:
        # Drop course if no course data for it exists
        filt_course = course_data.loc[course_data['course'] == course_filter]
        if len(filt_course.index) == 0:
            return None

        try:
            title = CourseTitle.get_course_title(course_filter)
            response['course_title'] = title
        except CourseTitle.DoesNotExist:
            pass

        try:
            section = get_course_details(course_filter)
        except (InvalidSectionID, DataFailureException):
            section = None

        try:
            response['course_description'] = section.course_description
        except AttributeError:
            pass

        prereqs_to = prereqs.loc[
            prereqs['course_to'] == course_filter
            ]
        prereqs_from = prereqs.loc[
            prereqs['course_from'] == course_filter
            ]
        prereqs = pd.concat([prereqs_to, prereqs_from])

    # remove self-loops and delete some extraneous fields
    prereqs.drop(prereqs[(prereqs.course_to == prereqs.course_from)].index,
                 inplace=True)
    prereqs.drop(list(prereqs.filter(regex='_spare')), axis=1, inplace=True)
    # prereqs.drop(columns = ['pr_last_update_dt'], inplace = True)

    course_data = course_data.loc[:, ['course',
                                      'department_abbrev',
                                      'course_number',
                                      'course_college',
                                      'long_course_title',
                                      'course_cat_omit']]

    # remove blacklisted currics
    cd_mask = course_data['department_abbrev'].isin(CURRIC_BLACKLIST)
    course_data = course_data[~cd_mask]
    pr_mask = prereqs['department_abbrev'].isin(CURRIC_BLACKLIST)
    prereqs = prereqs[~pr_mask]

    # remove graduate courses
    course_data = course_data[course_data.course_number < 500]

    # Remove 'retired' courses
    course_data = course_data[course_data.course_cat_omit == False]  # noqa

    # remove inactive courses from prereqs (keep them in the from field)
    prereqs = prereqs[prereqs['course_to'].isin(course_data['course'])]
    prereqs = prereqs[prereqs['course_from'].isin(course_data['course'])]

    # vertex metadata
    clist = prereqs[['course_to', 'course_from']].drop_duplicates()
    clist.sort_values(['course_to', 'course_from'], inplace=True)
    attribs = course_data[
        course_data['course'].isin(prereqs['course_to']) |
        course_data['course'].isin(prereqs['course_from'])
    ]

    ao = prereqs['pr_and_or'].apply(and_or)
    ao = prereqs['course_from'] + ao
    vlab_andor = ao.groupby(prereqs['course_to']).apply(lambda x: ' '.join(x))

    attribs = pd.merge(attribs, vlab_andor.to_frame(name="vlab_prereqs"),
                       how="left", left_on="course", right_on="course_to")
    attribs.vlab_prereqs = attribs.vlab_prereqs.fillna('')
    attribs['vlab'] = (attribs['long_course_title'] +
                       "<br>" + attribs['vlab_prereqs'])

    # re-structuring data for graph
    pr_obj = json.loads(prereqs.to_json())
    attr_obj = json.loads(attribs.to_json())

    edges = {}
    edges['from'] = pr_obj.get('course_from')
    edges['pr_and_or'] = pr_obj.get('pr_and_or')
    edges['pr_concurrency'] = pr_obj.get('pr_concurrency')
    edges['pr_cr_s'] = pr_obj.get('pr_cr_s')
    edges['pr_grade_min'] = pr_obj.get('pr_grade_min')
    edges['pr_group_no'] = pr_obj.get('pr_group_no')
    edges['pr_seq_no'] = pr_obj.get('pr_seq_no')
    edges['to'] = pr_obj.get('course_to')

    nodes = {}
    nodes['course.level'] = get_course_levels(attr_obj)
    nodes['course_branch'] = attr_obj.get('course_branch')
    nodes['course_cat_omit'] = attr_obj.get('course_cat_omit')
    nodes['course_college'] = attr_obj.get('course_college')
    nodes['course_number'] = attr_obj.get('course_number')
    nodes['course_title'] = attr_obj.get('long_course_title')
    nodes['department_abbrev'] = attr_obj.get('department_abbrev')
    nodes['diversity_crs'] = attr_obj.get('diversity_crs')
    nodes['english_comp'] = attr_obj.get('english_comp')
    nodes['indiv_society'] = attr_obj.get('indiv_society')
    nodes['natural_world'] = attr_obj.get('natural_world')
    nodes['qsr'] = attr_obj.get('qsr')
    nodes['vis_lit_perf_arts'] = attr_obj.get('vis_lit_perf_arts')
    nodes['writing_crs'] = attr_obj.get('writing_crs')

    options = {
        "height": "500px",
        "autoResize": True,
        "nodes": {
            "borderWidth": 1,
            "borderWidthSelected": 1,
            "shape": "box",
            "color": {
                "border": 'lightgray',
                "background": 'white',
                "highlight": {
                  "border": '#4d307f',
                  "background": '#976CE1'
                }
            }
        },
        "edges": {
            "arrows": "to",
            "smooth": {
                "type": 'cubicBezier',
                "forceDirection": 'horizontal',
                "roundness": 1
            },
            "color": 'lightgray'
        },
        "layout": {
            "hierarchical": {
                "direction": 'LR',
                "nodeSpacing": 80,
                "blockShifting": False,
                "edgeMinimization": False,
                "sortMethod": "directed"
            }
        },
        "interaction": {
            "dragNodes": False
        },
        "physics": False
    }

    response.update({'x': {'nodes': nodes,
                           'edges': edges,
                           'options': options}})

    if course_filter:
        data = json.dumps(response)
        if USE_CACHE:
            CourseGraphCache(graph_data=data, course_id=course_filter).save()
    if curric_filter:
        data = json.dumps(response)
        if USE_CACHE:
            CurricGraphCache(graph_data=data, curric_id=curric_filter).save()
    return response


# =============================================================================
# Build up the text string for the prereq relationships
#
# =============================================================================
def and_or(x=object):
    if x == "O":
        return " Or"
    elif x == "A":
        return "; and"
    else:
        return ""


def get_course_levels(attr_obj):
    numbers = attr_obj['course_number'].copy()
    for value in numbers:
        numbers[value] = course_level(numbers[value])
    return numbers


def course_level(course_number):
    return course_number - (course_number % 100)
