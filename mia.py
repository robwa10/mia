#------------------------ This is 79 characters--------------------------------

import csv
import datetime


f = open("feb2017.csv", "r").read()
rows = f.split('\n')

date_format = "%m-%d-%Y"
final_data = []

for i in rows:
    final_data.append(i.split(','))

del final_data[0] # Delete header row

for i in final_data:
    i[2] = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)


#for i in final_data:
#    trial = i[0]
#    if trial not in single_report:
#        single_report.append(i)


# -------------------------------------------------------------
# This is the sandbox area to test.

eric = final_data[:10]
temp = []

for i in eric:
    temp.append(i[2])


# End of sandbox area
# -------------------------------------------------------------

print(final_data[:20])
