# CSV Parsing and Comparison

A python script used to parse CSV attendance files and compare the data. Originally written to automate member attendance tracking.

Copyright 2017 Robert Hubbard.  
Licensed under the MIT License.  
Free for personal or educational use.  
All work is my own unless otherwise noted.

## Getting Started

**_Assumes you have python 3 installed on your computer_**  

Clone the repo:  
`git clone https://github.com/robwa10/mia.git`  

Cd into the repo: `cd mia`  

Run: `python3 weekly.py`

## Input Files  
The script is configured to accept CSV files only.  

All input files (with the exception of master_list.csv outputted by this script) should contain the following. Any additional columns are ignored:
- First Name column  
- Last Name column  
- Date column  

A sample master_list.csv and a second file, week_one.csv, are provided for you to test it's functionality.

## Script Purpose, Features and Functionality  

### Purpose
This script was originally written to automate the task of comparing attendance data. The following was needed on a weekly basis:  
- Members who had not attended for the previous two weeks.
- Members who had not attended for the previous four weeks.
- Members who had not attended for over four weeks.  

### Features  
The script can take in up to two files.
1. A master list containing member name and date of last attendance.
2. (Optional) A new CSV file containing new member attendance data.  

The following files are outputted.
1. A new master_list.csv containing the member name and most recent date of attendance.  
2. An Excel spreadsheet containing the names of members who haven't attending for the following time periods. Each time period is a separate sheet.
 - Two weeks
 - Four weeks  
 - Over four weeks


### Functionality  
The script is commented to aid in understanding it's functionality. However, here are some of the basic aspects of functionality.


- File data is parsed and converted into a dictionary with the name as the key and date as the value.  
- If the user inputs a second file that data is parsed and added to the dictionary. If a key already exists the value is updated to the most recent date attended.
- Dates in the dictionary are compared against today's date, appending the data to specific dicitionaries based on length between last attendance and today's date.
