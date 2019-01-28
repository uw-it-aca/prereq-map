#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pyodbc as po
import pandas as pd
#
# constring = open("utils/constring.txt").read()
# pwd = input("pwd...")
constring = "Driver={FreeTDS};Server=edwpub.s.uw.edu;Database=UWSDBDataStore;Port=1433;TDS_Version=7.2;UID=netid\\NETID;PWD=PASS"
con = po.connect(constring)

prereq = pd.read_sql('select * from sec.sr_course_prereq where last_eff_yr = 9999', con)
course_info = pd.read_sql('select * from sec.sr_course_titles where last_eff_yr = 9999', con)
print(course_info.columns)
con.close()

data_path = os.path.join(os.path.dirname(__file__),
                         '..',
                         'data')
prereq.to_pickle(os.path.join(data_path, "prereq_data.pkl"))
course_info.to_pickle(os.path.join(data_path, "course_data.pkl"))
