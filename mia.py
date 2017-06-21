import csv
import datetime as dt


f = open("feb2017.csv", "r").read()
rows = f.split('\n')

final_data = []
single_report = []

for i in rows:
    final_data.append(i.split(','))

del final_data[0] # Delete header row

#for i in rows:
#    final_data =  datetime.datetime.strptime(i[2], "%m/%d/%Y").strftime("%m/%d/%Y")

#for i in final_data:
#    trial = i[0]
#    if trial not in single_report:
#        single_report.append(i)

print(final_data[:11])
