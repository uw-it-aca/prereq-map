#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os
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
def process_data():
    data_path = os.path.join(os.path.dirname(__file__),
                             '..',
                             'data')

    os.chdir(os.getcwd())
    # vertex attributes
    course_data = pd.read_pickle(os.path.join(data_path, "course_data.pkl"))
    # edgelist
    prereqs = pd.read_pickle(os.path.join(data_path, "prereq_data.pkl"))

    # The database typically contains lots of whitespace for padding; remove it
    prereqs = prereqs.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    course_data = course_data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # create readable course from dept + #
    prereqs['course_to'] = prereqs['department_abbrev'] + " " + prereqs['course_number'].map(str)
    prereqs['course_from'] = prereqs['pr_curric_abbr'] + " " + prereqs['pr_course_no']

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




    attribs_json = attribs.to_json()
    prereq_json = prereqs.to_json()

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