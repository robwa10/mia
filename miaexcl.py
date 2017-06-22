import datetime
import openpyxl

#------------------------ This is 79 characters--------------------------------

wb = openpyxl.load_workbook('feb2017.xlsx')
ws = wb.worksheets[0]

print(ws)
