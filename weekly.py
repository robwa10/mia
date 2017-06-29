# ----------------------- This is 79 characters -------------------------------

import datetime
import csv
import xlsxwriter


# Global Variables
date_format = "%m/%d/%y"
date_long = "%m/%d/%Y"
today = datetime.datetime.today() 
file_date = datetime.datetime.today().strftime(date_long)
m_dict = {}
two_weeks = {}
four_weeks = {}
four_plus = {}
workbook = xlsxwriter.Workbook('MIA_Contact_List.xlsx')
sheet1 = workbook.add_worksheet('Two_Weeks')
sheet2 = workbook.add_worksheet('Four_Weeks')
sheet3 = workbook.add_worksheet('Four_Plus_Weeks')
row = 0
col = 0


def write_xl(my_dict, sheet):
    row = 0
    col = 0
    for k, v in sorted(my_dict.items()):
        sheet.write(row, col, k)
        sheet.write(row, col + 1, v)
        row += 1


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
    for i in a_list:
        name = i[fir] + ' ' + i[las]
        if name in m_dict:
            if m_dict[name]['last attendance'] < i[dt]:
                m_dict[name]['last attendance'] = i[dt]
        else:
            m_dict[name] = {'last attendance': i[dt]}


def master_dict(d, c, f):
    for i in d:
        m_dict[i[c]] = {'last attendance': i[f]}


def compare():
    for k in m_dict:
        m_date = m_dict[k]['last attendance']
        m_date = datetime.datetime.strptime(m_date, date_long)
        diff = (today - m_date).days
        if diff > 13 and diff < 16:
            two_weeks[k] = m_dict[k]['last attendance']
        elif diff > 29 and diff < 32:
            four_weeks[k] = m_dict[k]['last attendance']
        elif diff > 32:
            four_plus[k] = m_dict[k]['last attendance']


# User input of master file
master_file = input('Master filename >')
mas_name = 0
mas_date = 1
# Parsing and turning the master file into a dictionary
master_data = prep_file(master_file, mas_date, date_format)
master_dict(master_data, mas_name, mas_date)

# User input of comparison file
comparison_file = input('New filename >')
sec_fir_name = input('First Name column (e.g. 1,2,3...) >')
sec_fir = int(sec_fir_name) - 1
sec_las_name = input('Last Name column (e.g. 1,2,3...) >')
sec_las = int(sec_las_name) - 1
sec_date_col = input('Date column (e.g. 1,2,3...) >')
sec_date = int(sec_date_col) - 1
# Parsing and turning the comparison file into a dictionary
comp_file = prep_file(comparison_file, sec_date, date_long)
comp_dict = dict_create(comp_file, sec_fir, sec_las, sec_date)

compare()

write_xl(two_weeks, sheet1)
write_xl(four_weeks, sheet2)
write_xl(four_plus, sheet3)

workbook.close()
