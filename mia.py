#------------------------ This is 79 characters--------------------------------

import csv
import datetime


f = open("feb2017.csv", "r").read()
rows = f.split('\n')
del rows[0] # Delete header row

date_format = "%m-%d-%Y"
data = []
final_data = dict()
exit = 1

for i in rows:
    data.append(i.split(','))

for i in data:
    i[2] = datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime(date_format)
    if i[1] not in final_data:
        final_data[i[1]] = {'first': i[0], 'last': i[1], 'date': i[2], 'total': 1}
    else:
        exit += 1

#for i in data:
#    name = i[0] + " " + i[1]
#    if name in final_data:
#        final_data[name] = final_data[name] + date
#    else:
#        final_data[name] = date 

print(final_data)



# -------------------------------------------------------------
# This is the sandbox area to test.


# End of sandbox area
# -------------------------------------------------------------

