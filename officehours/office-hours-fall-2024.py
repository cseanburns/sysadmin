#!/usr/bin/env python3

from datetime import datetime

DAY = datetime.today().strftime("%A")

def office():
	if DAY == "Monday" or DAY == "Tuesday":
		print("""
		      Office hours for Dr. Sean Burns are from 1-3PM today.
		      """)
	else:
		print("""
		      No office hours today.
		      Please schedule an appointment:
			      EMAIL
			      PHONE_NUMBER
		      """)

office()
