# ----------------------- This is 79 characters -------------------------------
import datetime
import csv
from dateutil.parser import parse

# Global Variables
date_format = "%m/%d/%Y"
dict_errors = 0


def prep_file(a_file, n, secondary=False):
    """Read and split the csv on newline and comma and add to a list."""
    bar = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        bar.append(new)
    if secondary == True:
        for i in bar:
            i[n] = datetime.datetime.strptime(
                i[n], date_format).strftime(date_format)
    #print("This is the a_dict list.")
    #print(a_dict)
    return bar


def comparison_dict(a, fir, las, dt):
    """Turn the list into a dictionary of dictionaries."""
    a_dict = {} 
    for i in a:
        name = i[fir] + ' ' + i[las]
        if name in a_dict:
            if a_dict[name]['last attendance'] < i[dt]:
                a_dict[name]['last attendance'] = i[dt]
            a_dict[name]['total'] += 1
        elif name not in a_dict:
            a_dict[name] = {
                'last attendance': i[dt],
                'total': 1
                }
        else:
            dict_errors += 1
    return a_dict


def master_dict(d, c, f, x):
    m_dict = {}
    for i in d:
        m_dict[i[c]] = {
            'last attendance': i[f],
            'total': i[x]
            }
    return m_dict

# User input of master file
master_file = input('Master filename >')
mas_name = 0
mas_date = 1
mas_total = 2

# Parsing and turning the master file into a dictionary
master_data = prep_file(master_file, mas_date)
master_dictionary = master_dict(master_data, mas_name, mas_date, mas_total)

# User input of comparison file
secondary_file = input('comparison filename >')
sec_fir_name = input('First Name column (e.g. 1,2,3...) >')
sec_fir = int(sec_fir_name) - 1
sec_las_name = input('Last Name column (e.g. 1,2,3...) >')
sec_las = int(sec_las_name) - 1
sec_date_col = input('Date column (e.g. 1,2,3...) >')
sec_date = int(sec_date_col) - 1 

# Parsing and turning the comparison file into a dictionary
comp_file = prep_file(secondary_file, sec_date, secondary=True)
sec_dict = comparison_dict(comp_file, sec_fir, sec_las, sec_date)

"""
w = csv.writer(open("master_list", "w"))
for person, info in comp_file.items():
   w.writerow([person, info['last attendance'], info['total']])
"""
print(sec_dict)
print("You're files are waiting on you!")
print("You're total errors in creating dictionaries were %d." % dict_errors)
print(master_dictionary)
