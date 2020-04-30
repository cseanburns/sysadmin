#!/usr/bin/env python3

# Prints out office hours for the semester
#
# Print out the code and use it as the signage outside my office door

import os 
from datetime import datetime

officeday = datetime.today().strftime('%A')
day1     = "Tuesday"
day2     = "Wednesday"
email    = "myemail@uky.edu"
name     = "Sean Burns"
rank     = "Associate Professor"
unit     = "School of Information Science"
phone    = "859-555-0000"

os.system("clear")

print(f"Here works {name}, an {rank}")
print(f"at the {unit}.")
print(f'Today is {officeday}.')

if officeday == day1:
    print(f'If today is {day1}, then my office hours are 1-3pm.')
elif officeday == day2:
    print(f'If today is {day2}, then my office hours are 1-3pm.')
else:
    print(f'If {officeday} is not {day1} or is not {day2},')
    print('then I do not have office hours today. Please knock on door')
    print(f'or email me at {email} or call me at {phone}')
    print('to schedule an appointment.')
