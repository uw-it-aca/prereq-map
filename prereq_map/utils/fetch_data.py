#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyodbc as po
import pandas as pd

constring = open("utils/constring.txt").read()
pwd = input("pwd...")

con = po.connect(constring+pwd)

prereq = pd.read_sql('select * from sec.sr_course_prereq where last_eff_yr = 9999', con)
course_info = pd.read_sql('select * from sec.sr_course_titles where last_eff_yr = 9999', con)

con.close()

prereq.to_pickle("data/prereq_data.pkl")
course_info.to_pickle("data/course_data.pkl")

del [con, constring, prereq, course_info, pwd]
