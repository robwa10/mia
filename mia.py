# ----------------------- This is 79 characters -------------------------------
import datetime
import csv


# Global Variables
date_format = "%m/%d/%Y"
dict_errors = 0


def prep_file(a_file):
    """Read and split the csv on newline and comma and add to a list."""
    bar = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        new = i.split(',')
        bar.append(new)
    #print("This is the a_dict list.")
    #print(a_dict)
    return bar


def format_date(foo, n):
    """Format the dates in each list for comparison later."""
    for i in foo:
        i[n] = datetime.datetime.strptime(
            i[n], date_format).strftime(date_format)
    #print("\n\n\nThis is the data list after time formatting.")
    #print(data)
    return foo


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


# User input of comparison file
secondary_file = input('comparison filename >')
sec_fir_name = input('First Name column (e.g. 1,2,3...) >')
sec_fir = int(sec_fir_name) - 1
sec_las_name = input('Last Name column (e.g. 1,2,3...) >')
sec_las = int(sec_las_name) - 1
sec_date_col = input('Date column (e.g. 1,2,3...) >')
sec_date = int(sec_date_col) - 1 
comp_file = prep_file(secondary_file)
new_data = format_date(comp_file, sec_date)
sec_dict = comparison_dict(new_data, sec_fir, sec_las, sec_date)

"""
w = csv.writer(open("master_list", "w"))
for person, info in comp_file.items():
   w.writerow([person, info['last attendance'], info['total']])
"""
print("You're files are waiting on you!")
print("You're total errors in creating dictionaries were %d." % dict_errors)
