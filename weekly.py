# ----------------------- This is 79 characters -------------------------------

import datetime
import csv
import xlsxwriter
import answervalid as av


# Global Variables
date_format = "%m/%d/%y"
date_long = "%m/%d/%Y"
today = datetime.datetime.today() 
m_dict = {}
two_weeks = {}
four_weeks = {}
four_plus = {}
master = {}
workbook = xlsxwriter.Workbook('MIA_Contact_List.xlsx')
sheet4 = workbook.add_worksheet('Master_List')
sheet1 = workbook.add_worksheet('Two_Weeks')
sheet2 = workbook.add_worksheet('Four_Weeks')
sheet3 = workbook.add_worksheet('Four_Plus_Weeks')


def file_vars():
    a_file = input('Filename >')
    fir = int(input('First Name column (e.g. 1,2,3...) >')) - 1
    las = int(input('Last Name column (e.g. 1,2,3...) >')) - 1
    file_date = int(input('Date column (e.g. 1,2,3...) >')) - 1
    mas_file = prep_file(a_file, file_date, date_long )
    dict_create(mas_file, fir, las, file_date)


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
        new_date = datetime.datetime.strptime(m_date, date_long)
        diff = (today - new_date).days
        if diff > 13 and diff < 16:
            two_weeks[k] = m_date
        elif diff > 29 and diff < 32:
            four_weeks[k] = m_date
        elif diff > 31:
            four_plus[k] = m_date
        master[k] = m_date

def write_files():
    write_xl(master, sheet4)
    write_xl(two_weeks, sheet1)
    write_xl(four_weeks, sheet2)
    write_xl(four_plus, sheet3)


def write_xl(my_dict, sheet):
    row = 0
    col = 0
    for k, v in sorted(my_dict.items()):
        sheet.write(row, col, k)
        sheet.write(row, col + 1, v)
        row += 1


# User input of master file
print("Do you have a master file?")
choice = av.yes_no()
if choice == 'y':
    master_file = input('Master filename >')
    mas_name = 0
    mas_date = 1
    # Parsing and turning the master file into a dictionary
    master_data = prep_file(master_file, mas_date, date_long)
    master_dict(master_data, mas_name, mas_date)
if choice == 'n':
    file_vars()

# Input of new data
print("Load another file to update master list?")
choice = av.yes_no()
if choice == 'y':
    file_vars()
    compare()
else:
    compare()

write_files()
workbook.close()
print("You're files are waiting for you.")
