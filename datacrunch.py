import csv
import sys

import sqlite3
# some help
# https://www.tutorialspoint.com/sqlite/sqlite_insert_query.htm

# connection
# conn = sqlite3.connect('worktree.db')
#
# # cursor
# cur = conn.cursor()
#
# # print (sys.version)
# #
# a = open('neisdatagovhack.csv', 'r')
#
# reader = csv.reader(a)
#
# string = "INSERT INTO neisdatagovhack (business_id, start_date, end_date, neis_type, exit_reason, successful, anzsic_code, industry_type, state, metro, age_group, gender_cd, indigenous_ind, ex_offender_ind, nesb_ind, refugee_ind, disability_ind, homeless_ind, sole_parent_ind, neis_allowance_ind, surveyed, sv_month, sv_year, sv_in_operation, sv_hours_work, sv_staff_lt35h, sv_staff_gt35h, sv_end_train, sv_end_mentor, sv_end_profit, sv_end_dem, sv_end_loc, sv_end_health, sv_end_oth, sv_sat_bus_train, sv_sat_mentor, sv_tailor_sup, sv_sat_overall ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
#
# z = 0
# for i in (reader):
#
#     if z == 0:
#         z += 1
#         continue
#     j = tuple(i)
#
#
#     cur.execute(string, j)
#
#
#
# conn.commit()
#
# conn.close()


# a= ['business_id', 'start_date', 'end_date', 'neis_type', 'exit_reason', 'successful', 'anzsic_code', 'industry_type', 'state', 'metro', 'age_group', 'gender_cd', 'indigenous_ind', 'ex_offender_ind', 'nesb_ind', 'refugee_ind', 'disability_ind', 'homeless_ind', 'sole_parent_ind', 'neis_allowance_ind', 'surveyed', 'sv_month', 'sv_year', 'sv_in_operation', 'sv_hours_work', 'sv_staff_lt35h', 'sv_staff_gt35h', 'sv_end_train', 'sv_end_mentor', 'sv_end_profit', 'sv_end_dem', 'sv_end_loc', 'sv_end_health', 'sv_end_oth', 'sv_sat_bus_train', 'sv_sat_mentor', 'sv_tailor_sup', 'sv_sat_overall']
# string =      '''CREATE TABLE neisdatagovhack (business_id INTEGER PRIMARY KEY AUTOINCREMENT, '''
# for i, j in enumerate(a):
#     if i == 0:
#         continue
#     else:
#         string +=  j + ' TEXT, '

# import sqlite3
# # some help
# # https://www.tutorialspoint.com/sqlite/sqlite_insert_query.htm
#
# # connection
# conn = sqlite3.connect('worktree.db')
#
# # cursor
# cur = conn.cursor()
#
# # Create table
# # string = 'CREATE TABLE neisdatagovhack (business_id INTEGER PRIMARY KEY AUTOINCREMENT, start_date TEXT, end_date TEXT, neis_type TEXT, exit_reason TEXT, successful TEXT, anzsic_code TEXT, industry_type TEXT, state TEXT, metro TEXT, age_group TEXT, gender_cd TEXT, indigenous_ind TEXT, ex_offender_ind TEXT, nesb_ind TEXT, refugee_ind TEXT, disability_ind TEXT, homeless_ind TEXT, sole_parent_ind TEXT, neis_allowance_ind TEXT, surveyed TEXT, sv_month TEXT, sv_year TEXT, sv_in_operation TEXT, sv_hours_work TEXT, sv_staff_lt35h TEXT, sv_staff_gt35h TEXT, sv_end_train TEXT, sv_end_mentor TEXT, sv_end_profit TEXT, sv_end_dem TEXT, sv_end_loc TEXT, sv_end_health TEXT, sv_end_oth TEXT, sv_sat_bus_train TEXT, sv_sat_mentor TEXT, sv_tailor_sup TEXT, sv_sat_overall TEXT )'
# string = 'CREATE TABLE neisdatagovhack (business_id INTEGER PRIMARY KEY AUTOINCREMENT, start_date TEXT, end_date TEXT, neis_type TEXT, exit_reason TEXT, successful TEXT, anzsic_code INTEGER, industry_type TEXT, state TEXT, metro INTEGER, age_group TEXT, gender_cd TEXT, indigenous_ind TEXT, ex_offender_ind TEXT, nesb_ind TEXT, refugee_ind TEXT, disability_ind TEXT, homeless_ind TEXT, sole_parent_ind TEXT, neis_allowance_ind TEXT, surveyed TEXT, sv_month INTEGER, sv_year INTEGER, sv_in_operation INTEGER, sv_hours_work INTEGER, sv_staff_lt35h INTEGER, sv_staff_gt35h INTEGER, sv_end_train TEXT, sv_end_mentor TEXT, sv_end_profit TEXT, sv_end_dem TEXT, sv_end_loc TEXT, sv_end_health TEXT, sv_end_oth TEXT, sv_sat_bus_train INTEGER, sv_sat_mentor INTEGER, sv_tailor_sup INTEGER, sv_sat_overall INTEGER )'
# cur.execute(string)
#
# conn.commit()
#
# conn.close()

# create insert tuple
# s
# string = '('
# for i, j in enumerate(a):
#
#         string +=  '?, '

# string = "INSERT INTO neisdatagovhack "
#
# string += '(business_id, start_date, end_date, neis_type, exit_reason, successful, anzsic_code, industry_type, state, metro, age_group, gender_cd, indigenous_ind, ex_offender_ind, nesb_ind, refugee_ind, disability_ind, homeless_ind, sole_parent_ind, neis_allowance_ind, surveyed, sv_month, sv_year, sv_in_operation, sv_hours_work, sv_staff_lt35h, sv_staff_gt35h, sv_end_train, sv_end_mentor, sv_end_profit, sv_end_dem, sv_end_loc, sv_end_health, sv_end_oth, sv_sat_bus_train, sv_sat_mentor, sv_tailor_sup, sv_sat_overall )'
#
# string += " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
#
# print (string)

# SELECT * FROM neisdatagovhack WHERE anzsic_code > x and anzsic_code < y



################Turn  json

# result needed:
# "list" : [
#             {
#                 "name" : "Agriculture",
#                 "min" : 1,
#                 "max" : 19
#             }
#         ]

a = [
["Repair and Maintenance",9400,9499],
["Personal and Other Services",9500,9599],
["Private Households Employing Staff and Undifferentiated Goods and Service-Producing Activities of Households for\
Own Use",9600,9699],
]
list = {"list" : []}

from pprint import pprint
for i in a:

    g = {
        "name" : i[0],
        "min" : i[1],
        "max" : i[2]
         }

    list.get("list").append(g)


import json
print (json.dumps(list))



