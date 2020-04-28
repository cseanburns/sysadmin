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

if officeday == day1:
    print("\nSince today is {}, my office hours are 1-3pm".format(day1))
elif officeday == day2:
    print("\nSince today is {}, my office hours are 1-3pm".format(day2))
else:
    print("\nSince today is neither {} nor {},".format(day1,day2))
    print("please knock on door or email me at {}".format(email))
    print("to schedule an appointment.")
