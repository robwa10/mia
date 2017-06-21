#------------------------ This is 79 characters--------------------------------

import csv
import datetime


f = open("feb2017.csv", "r").read()
rows = f.split('\n')
del rows[0] # Delete header row

date_format = "%m-%d-%Y"
final_data = []
full_name = []
date = []

#for i in rows:
#    final_data.append(i.split(','))

#del final_data[0] # Delete header row

#for i in final_data:
#    i[2] = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)


#for i in final_data:
#    trial = i[0]
#    if trial not in single_report:
#        single_report.append(i)


# -------------------------------------------------------------
# This is the sandbox area to test.

for i in rows:
    full_name.append(i[0] + i[1])
#    date = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)

print(full_name[:20])
#print(date[:20])

# End of sandbox area
# -------------------------------------------------------------

