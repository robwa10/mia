**CSV Parsing and Comparison**

This program is used to parse csv files and compare the data for attendance tracking. Feel free to copy the repo and adjust to suit your own needs. It is of course run in the command line.

Here is what it does:
1.  User inputs a csv. Specifying which columns contain first name, last name and date.
2. Parses the csv, turning the data into a dictionary.
3. User inputs a master csv, again speciying columns.
4. Parses the csv into a dictionary.
5. Compares the two dictionaries.
6. Produces a .txt file with anyone who hasn't attended in the last two weeks.
7. Produces a .txt file with anyone who hasn't attend in the last four weeks.
8. Produces a .txt file with anyone who hasn't attended in over four weeks.
9. Writes a new master attendance csv file for future comparion that contains:
    - First Name
    - Last Name
    - Date last attended
    - Total number of attendances
