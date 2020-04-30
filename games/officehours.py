#!/usr/bin/env python3

# Prints out office hours for the semester
#
# Print out the code and use it as the signage outside my office door

import os 
from datetime import datetime

officeday = datetime.today().strftime('%a')
day1 = "Tue"
day2 = "Wed"
email = "myemail@uky.edu"

os.system("clear")
print("Christopher Sean Burns, PhD")
print("Associate Professor")
print(email)
print("859-555-0000")
print("Spring 2020")
print("")

if officeday == day1:
    print(f'Since today is {day1}, my office hours are 1-3pm')
elif officeday == day2:
    print(f'Since today is {day2}, my office hours are 1-3pm')
else:
    print(f'Since today is neither {day1} nor {day2},')
    print('please knock on door or email me at')
    print(f'{email} to schedule an appointment.')
    print("")
