#------------------------ This is 79 characters--------------------------------

import csv
import datetime


f = open("feb2017.csv", "r").read()
rows = f.split('\n')
del rows[0] # Delete header row

date_format = "%m-%d-%Y"
data = []
full_name = []
date = []
final_data = dict()

for i in rows:
    data.append(i.split(','))

for i in data:
    date = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)
    name = i[0] + " " + i[1]
    if name in final_data:
        final_data[name] = final_data[name] + date
    else:
        final_data[name] = date 

print(final_data)

#del final_data[0] # Delete header row

#for i in final_data:
#    i[2] = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)


#for i in final_data:
#    trial = i[0]
#    if trial not in single_report:
#        single_report.append(i)


# -------------------------------------------------------------
# This is the sandbox area to test.

#print(date[:20])

# End of sandbox area
# -------------------------------------------------------------

