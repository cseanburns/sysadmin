#!/usr/bin/env python3
"""
This is silly way to post my office hours. Print out the code and post it as
signage outside my office door.
"""

import os
from datetime import datetime

OFFICEDAY = datetime.today().strftime('%A')
DAY1 = "Tuesday"
DAY2 = "Wednesday"
EMAIL = "myemail@uky.edu"
NAME = "Sean Burns"
RANK = "Associate Professor"
UNIT = "School of Information Science"
PHONE = "859-555-0000"

os.system("clear")

print(f"Here works {NAME}, an {RANK}")
print(f"at the {UNIT}.\n")
print(f'Today is {OFFICEDAY}.\n')

if OFFICEDAY == DAY1:
    print(f'If today is {DAY1}, then my office hours are 1-3pm.')
elif OFFICEDAY == DAY2:
    print(f'If today is {DAY2}, then my office hours are 1-3pm.')
else:
    print(f'If {OFFICEDAY} is not {DAY1} or is not {DAY2},')
    print('then I do not have office hours today.\n')
    print(f'Please knock on door, email me at {EMAIL},')
    print(f'or call me at {PHONE} to schedule an appointment.')
