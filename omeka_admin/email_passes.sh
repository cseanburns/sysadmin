#!/usr/bin/env bash

# Date: Wed Oct  6 09:50:00 AM EDT 2021
# Author: sean
# A simple script to email temporary passes to users
# Need to add a sleep command to prevent too many emails at one time
# Need to add a short message, that includes NAME, that explains the email
# Assumes a CSV file that looks like this:
# 
# name, email, pass, CC
#
# Note: I haven't used this yet.
# Colleagues have wanted to share passes themselves.

while read -r line ; do
  TO=$(echo "$line" | awk -F',' '{print $2}')
  PASS=$(echo "$line" | awk -F',' '{print $3}')
  CC=$(echo "$line" | awk -F',' '{print $4}')
  echo "$PASS" | mutt -c "$CC" -s "Server info" "$TO" 
done < email_list.csv 
