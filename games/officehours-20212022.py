#!/usr/bin/env python3
"""
This is silly way to post my office hours. Print out the code and post it as
signage outside my office door.
For Fall 2021
"""

import os
from datetime import datetime

DAY = datetime.today().strftime('%a')
OFFICEDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")
WEEKEND = ("Sat", "Sun")
EMAIL = "myemail@uky.edu"
NAME = "Sean Burns"
RANK = "Associate Professor"
UNIT = "School of Information Science"
PHONE = "859-555-0000"

os.system("clear")

print(f"Here works {NAME}, an {RANK} at the {UNIT}.\n")
print(f"Today is {DAY}.\n")

if DAY in OFFICEDAYS:
    print(f"If today is {DAY}, then I am available.\n")
    print(f"Please knock on door, email me at {EMAIL}, or call at {PHONE}.")
elif DAY in WEEKEND:
    print(f"If today is {DAY}, then I am not available.\n")
    print(f"Also, how are you in this building on a {DAY}?\n")
    print(f"Otherwise, email me at {EMAIL} or call and leave a message at {PHONE}.")
else:
    print("I am not available during breaks, etc.")
