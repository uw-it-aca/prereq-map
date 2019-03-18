#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os
import json
# import igraph as ig

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
def process_data(curric_filter=None, course_filter=None):
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')

    # vertex attributes
    course_data = pd.read_pickle(os.path.join(data_path, "course_data.pkl"))
    # edgelist
    prereqs = pd.read_pickle(os.path.join(data_path, "prereq_data.pkl"))

    # The database typically contains lots of whitespace for padding; remove it
    prereqs = prereqs.apply(
        lambda x: x.str.strip() if x.dtype == "object" else x)
    course_data = course_data.apply(
        lambda x: x.str.strip() if x.dtype == "object" else x)
    # create readable course from dept + #
    prereqs['course_to'] = prereqs['department_abbrev'] + " " + prereqs[
        'course_number'].map(str)
    prereqs['course_from'] = prereqs['pr_curric_abbr'] + " " + prereqs[
        'pr_course_no']

    if curric_filter:
        course_data = course_data.loc[
            course_data['department_abbrev'] == curric_filter]
        prereqs = prereqs.loc[
            prereqs['department_abbrev'] == curric_filter]

    if course_filter:
        prereqs_to = prereqs.loc[
            prereqs['course_to'] == course_filter
            ]
        prereqs_from = prereqs.loc[
            prereqs['course_from'] == course_filter
            ]
        prereqs = pd.concat([prereqs_to, prereqs_from])




    course_data['course'] = course_data['department_abbrev'] + " " + course_data['course_number'].map(str)

    # remove self-loops and delete some extraneous fields
    prereqs.drop(prereqs[(prereqs.course_to == prereqs.course_from)].index, inplace = True)
    prereqs.drop(list(prereqs.filter(regex = '_spare')), axis = 1, inplace = True)
    # prereqs.drop(columns = ['pr_last_update_dt'], inplace = True)

    course_data = course_data.loc[:, ['course', 'department_abbrev', 'course_number',
                                      'last_eff_yr', 'last_eff_qtr', 'course_branch',
                                      'course_college', 'long_course_title',
                                      'prq_lang_of_adm', 'prq_check_grads', 'pre_cancel_req',
                                      'course_cat_omit', 'writing_crs', 'diversity_crs',
                                      'english_comp', 'qsr', 'vis_lit_perf_arts',
                                      'indiv_society', 'natural_world']]

    # remove inactive courses from prereqs (keep them in the from field)
    # prereqs = prereqs[prereqs['course_from'].isin(course_data['course'])]
    prereqs = prereqs[prereqs['course_to'].isin(course_data['course'])]

    # vertex metadata
    clist = prereqs[['course_to', 'course_from']].drop_duplicates()
    clist.sort_values(['course_to', 'course_from'], inplace = True)

    attribs = course_data[course_data['course'].isin(prereqs['course_to']) | course_data['course'].isin(prereqs['course_from'])]


    ao = prereqs['pr_and_or'].apply(and_or)
    ao = prereqs['course_from'] + ao
    vlab_andor = ao.groupby(prereqs['course_to']).apply(lambda x: ' '.join(x))

    attribs = pd.merge(attribs, vlab_andor.to_frame(name = "vlab_prereqs"),
                    how = "left", left_on = "course", right_on = "course_to")
    attribs.vlab_prereqs = attribs.vlab_prereqs.fillna('')
    attribs['vlab'] = attribs['long_course_title'] + "<br>" + attribs['vlab_prereqs']

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
        # "width": "100%",
        "height": "500px",      # [TODO] Fix.this
        # "height": "100%",
        "autoResize": True,
        "nodes": {
            "shape": "circle",
            "size": 20,
            "color": {
                "background": "lime",
                "border": "black"
            },
        },
        "edges": {
            "arrows": "to",
            "color": "gray"
        },
        "layout": {
            "hierarchical": {
                "enabled": True,
                "direction": "DU"
            },
        },
        "interaction":{
            "multiselect": True
        }
    }
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
    response.update({'x': {'nodes': nodes,
                           'edges': edges,
                           'options': options}})
    return response
=======

    # options = {
    #     "width": "100%",
    #     "height": "100%",
    #     "nodes": {
    #         "physics": False,
    #         "shape": "circle",
    #         "size": 2,
    #         "font": {
    #             "size": 17
    #         }
    #     },
    #     "manipulation": {
    #         "enabled": False
    #     },
    #     "edges": {
    #         "smooth": False,
    #         "arrows": "to"
    #     },
    #     "physics": {
    #         "stabilization": False
    #     },
    #     "interaction": {
    #         "hideEdgesOnDrag": True,
    #         "hoverConnectedEdges": True,
    #         "multiselect": True
    #     },
    #     "layout": {
    #         "hierarchical": {
    #             "enabled": True,
    #             "levelSeparation": 40,
    #             "nodeSpacing": 150,
    #             "direction": "LR"
    #         },
    #         "improvedLayout": False
    #     },
    # }
>>>>>>> Stashed changes

    return {'x': {'nodes': nodes,
                  'edges': edges,
                  'options': options}}
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
>>>>>>> Stashed changes


# =============================================================================
# Build up the text string for the prereq relationships
#
# =============================================================================
def and_or(x = object):
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
