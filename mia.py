import csv
import datetime as dt


f = open("feb2017.csv", "r").read()
rows = f.split('\n')

final_data = []
single_report = []

for i in rows:
    final_data.append(i.split(','))

for i in final_data:
    trial = i[0]
    if trial not in single_report:
        single_report.append(i)

print(single_report[:11])