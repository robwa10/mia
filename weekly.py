# ----------------------- This is 79 characters -------------------------------
from dateutil.parser import *
from dateutil.tz import *
import datetime
import csv
import xlsxwriter

# Global Variables
date_short = "%m/%d/%y"
date_long = "%m/%d/%Y"
today = datetime.datetime.today()
m_dict = {}
two_weeks = {}
four_weeks = {}
four_plus = {}
master = {}

def yes_no():
    """Ask user Yes or No and validate the answer."""
    message = '[Y/N] >'
    answer = input(message).lower()
    while answer not in ['y', 'n']:
        answer = input("Choose [Y/N] >").lower()
    return answer


def file_vars():
    """Allow user to specify which column each set of data is contained in."""
    a_file = input('Filename >')
    fir = int(input('First Name column (e.g. 1,2,3...) >')) - 1
    las = int(input('Last Name column (e.g. 1,2,3...) >')) - 1
    file_date = int(input('Date column (e.g. 1,2,3...) >')) - 1
    print('Does your file have a header?')
    choice = yes_no()
    if choice == 'y':
        header = True
    else:
        header = False
    mas_file = prep_file(a_file, file_date, header)
    dict_create(mas_file, fir, las, file_date)


def prep_file(a_file, n, header):
    """Read and split the csv on newline and comma then add to a list."""
    new_list = []
    f = open(a_file, 'r').read()
    rows = f.split('\n')
    for i in rows:
        line = i.rstrip()
        if line:
            new = line.split(',')
            new_list.append(new)
    if header is True:
        del new_list[0]
    for i in new_list:
        x = parse(i[n])
        x = x.strftime(date_long)
        i[n] = x
    return new_list


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
    """Turn master_file into dictionary."""
    for i in d:
        m_dict[i[c]] = {'last attendance': i[f]}


def compare():
    """Compare m_dict dates to today's date and append to appropriate dict."""
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
    """Write Excel file containg data for those needing to be contacted and
    write a new master list with updated data."""
    workbook = xlsxwriter.Workbook('Contact_List.xlsx')
    sheet1 = workbook.add_worksheet('Two_Weeks')
    sheet2 = workbook.add_worksheet('Four_Weeks')
    sheet3 = workbook.add_worksheet('Four_Plus_Weeks')
    sheet4 = workbook.add_worksheet('All_Data')
    w = csv.writer(open("master_list.csv", "w"))
    write_xl(two_weeks, sheet1)
    write_xl(four_weeks, sheet2)
    write_xl(four_plus, sheet3)
    write_xl(master, sheet4)
    for k, v in sorted(master.items()):
        w.writerow([k, v])
    workbook.close()
    return w


def write_xl(my_dict, sheet):
    """Write Excel sheets."""
    row = 0
    col = 0
    for k, v in sorted(my_dict.items()):
        sheet.write(row, col, k)
        sheet.write(row, col + 1, v)
        row += 1


# User input of master file.
print(
    "Do you have a master file previously outputted by this script "
    "that is also in this directory?"
    )
if yes_no() == 'y':
    master_dict(prep_file('master_list.csv', 1, header=False), 0, 1)
else:
    file_vars()

# Check if the user has a file containing new data.
print("Load another file to update master list?")
if yes_no() == 'y':
    file_vars()
    compare()
else:
    compare()

# Write the Excel file with the contact list data.
# Write the new master_list.csv file.
write_files()
print("Success! You're files are waiting for you.")
