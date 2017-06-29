# ----------------------- This is 79 characters -------------------------------

import datetime
import csv


# Global Variables
date_format = "%m/%d/%y"
date_long = "%m/%d/%Y"
dict_errors = 0
dict_check = 0
two_weeks = {} 
four_weeks = {}


def prep_file(a_file, n, d):
    """Read and split the csv on newline and comma and add to a list."""
    bar = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        bar.append(new)
    for i in bar:
        i[n] = datetime.datetime.strptime(
            i[n], d).strftime(date_long)
    return bar


def dict_create(a_list, fir, las, dt):
    """Turn the list into a dictionary of dictionaries."""
    a_dict = {} 
    for i in a_list:
        name = i[fir] + ' ' + i[las]
        if name in a_dict:
            if a_dict[name]['last attendance'] < i[dt]:
                a_dict[name]['last attendance'] = i[dt]
        else:
            a_dict[name] = {'last attendance': i[dt]}
    return a_dict


def master_dict(d, c, f):
    m_dict = {}
    for i in d:
        m_dict[i[c]] = {'last attendance': i[f]}
    return m_dict


def dict_compare():
    for k in comp_dict:
        if k in master_dictionary:
            if comp_dict[k]['last attendance'] > master_dictionary[
                k]['last attendance']:
                new_date = comp_dict[k]['last attendance']
                old_date = master_dictionary[k]['last attendance']
                new_date = datetime.datetime.strptime(new_date, date_long)
                old_date = datetime.datetime.strptime(old_date, date_long)
                diff = (new_date - old_date).days
                if diff > 13 and diff < 16:
                    two_weeks[k] = comp_dict[k]['last attendance']
                elif diff > 29 and diff < 32:
                    four_weeks[k] = comp_dict[k]['last attendance']
                master_dictionary[k] = comp_dict[k]['last attendance']
            else:
                dict_check += 1
        else:
            master_dictionary[k] = comp_dict[k]['last attendance']


# User input of master file
master_file = input('Master filename >')
mas_name = 0
mas_date = 1
# Parsing and turning the master file into a dictionary
master_data = prep_file(master_file, mas_date, date_format)
master_dictionary = master_dict(master_data, mas_name, mas_date)

# User input of comparison file
comparison_file = input('comparison filename >')
sec_fir_name = input('First Name column (e.g. 1,2,3...) >')
sec_fir = int(sec_fir_name) - 1
sec_las_name = input('Last Name column (e.g. 1,2,3...) >')
sec_las = int(sec_las_name) - 1
sec_date_col = input('Date column (e.g. 1,2,3...) >')
sec_date = int(sec_date_col) - 1 
# Parsing and turning the comparison file into a dictionary
comp_file = prep_file(comparison_file, sec_date, date_long)
comp_dict = dict_create(comp_file, sec_fir, sec_las, sec_date)

"""
w = csv.writer(open("master_list", "w"))
for person, info in comp_file.items():
   w.writerow([person, info['last attendance'], info['total']])
"""

dict_compare()

print("You're files are waiting on you!")
print("You're total errors in creating dictionaries were %d." % dict_errors)
print("dict_check: %d." % dict_check)
print("2 weeks: %r" % two_weeks)
print("4 weeks: %r" % four_weeks)
