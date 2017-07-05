**CSV Parsing and Comparison**

This program is used to parse csv files and compare the data for attendance tracking. Feel free to copy the repo and adjust to suit your own needs. It is of course run in the command line.

Here is what it does:
1.  User inputs a csv. Specifying which columns contain first name, last name, date and the format of the date.
2. Parses the csv, turning the data into a dictionary.
3. User inputs another csv, again speciying data format.
4. Parses the csv and adds the data to the dictionary.
5. Compares the dates in the dictionary to today's date, appending the data to specific dicitionaries based on length between last attendance and today's date.
6. Writes an .xlsx file with the following sheets.
    - Anyone who hasn't attended in the last two weeks.
    - Anyone who hasn't attend in the last four weeks.
    - Anyone who hasn't attended in over four weeks.
    - All attendance data.
7. Writes a new master attendance .csv file for future comparion that contains:
    - Full Name
    - Date last attended
