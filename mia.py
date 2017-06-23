# ----------------------- This is 79 characters -------------------------------
import datetime
import csv


date_format = "%m-%d-%Y"
final_data = dict()
dict_errors = 0
master_list = []
w = csv.writer(open("master_list.csv", "w"))

# User input of master file, open, read and split on ','
x = input('master filename >')
master_file = file_input(x)

"""
# User input of comparison file, open, read, split and delete header row
secondary_file = input('comparison filename >')
comp_file = file_input(secondary_file)
del comp_file[0]
"""

def file_input(a_file):
    f = open(a_file, "r").read()
    f = f.split("\n")
    return f

for i in rows:
    data = [i.split(',')]
    for i in data:
        i[2] = datetime.datetime.strptime(
            i[2], "%m/%d/%Y"
            ).strftime(date_format)  # Change string to date format
        name = i[0] + ' ' + i[1]
        if name in final_data:
            if final_data[name]['date'] < i[2]:
                final_data[name]['date'] = i[2]
            final_data[name]['total'] = final_data[name]['total'] + 1
        elif name not in final_data:
            final_data[name] = {
                'date': i[2],
                'total': 1
                }
        else:
            dict_errors += 1

# for person, info in final_data.items():
#    w.writerow([person, info['date'], info['total']])
#    master_list.append([person, info['date'], info['total']])

# tf = open("attendance_data.txt", "w")
# tf.close()
