# ----------------------- This is 79 characters -------------------------------
import datetime
import csv


date_format = "%m/%d/%Y"
final_data = dict()
dict_errors = 0
master_list = []
w = csv.writer(open("master_list", "w"))


def prep_file(a_file):
    """Read and split the csv on newline and comma and add to a list."""
    final_data = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        final_data.append(new)
    print("This is the final_data list.")
    print(final_data)
    return final_data

def format_date(data):
    for i in data:
        i[2] = datetime.datetime.strptime(
            i[2], date_format).strftime(date_format)
    print("\n\n\nThis is the data list after time formatting.")
    print(data)
    return data
    
"""
def parse_file(a_file, x, secondary=True):
                name = i[1] + ' ' + i[0]
                if name in data_dict:
                    if data_dict[name]['last attendance'] < i[x]:
                       data_dict[name]['last attendance'] = i[x]
                    data_dict[name]['total'] += 1
                elif name not in data_dict:
                    data_dict[name] = {
                        'last attendance': i[x],
                        'total': 1
                        }
                else:
                    dict_errors += 1
        else:
            for i in data:
                i[x] = datetime.datetime.strptime(
                    i[x], "%m-%d-%Y"
                    ).strftime(date_format)
                data_dict[i[0]] = {
                    'date': i[1],
                    'total': i[2]
                    }
    return data_dict
"""

# User input of comparison file, open, read, split and delete header row
secondary_file = input('comparison filename >')
comp_file = prep_file(secondary_file)
comp_date = format_date(comp_file)
print("The secondary data was returned.")
print(comp_date)


"""
for person, info in comp_file.items():
   w.writerow([person, info['last attendance'], info['total']])

# User input of master file, open, read and split on ','
master = input('master filename >')
master_data = prep_file(master)
#master_data = master_data.pop()

print("The master data was returned.")
print(master_data)
"""

# tf = open("attendance_data.txt", "w")
# tf.close()
