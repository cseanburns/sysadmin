#!/bin/bash

# Date: Fri Sep 14 13:44:47 EDT 2018
# Description: When batch creating new accounts, this script will
# first check to see if the account names listed in the file 
# "user_list_file.csv" are already in the system
# "user_list_file.csv" contains a list of candidate user accounts

userfile="user_list_file.csv"

# Get list of current account user names and save to file current_accounts.txt
cat /etc/passwd | cut -d: -f1 > current_accounts.txt

# cat the above file to a file containing a list of pre-existing new accounts
# to create
cat current_accounts.txt "$userfile" > all_accounts.txt

# sort the user names in the new file and only print duplicate lines
sort all_accounts.txt | uniq -d > duplicates.txt

# These are the accounts you will need to add
# This "users_to_add.txt" can be sent to the 'create_accounts' script
cat duplicates.txt "$userfile" | sort | uniq -u > users_to_add.txt

# remove uneeded files
rm current_accounts.txt all_accounts.txt duplicates.txt