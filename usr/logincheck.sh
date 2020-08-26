#!/bin/bash
# Date: 2020-08-24

# check to see if users are logging in and running commands
# run as root and put in crontab
# file 'accountsnames' includes user accounts, one line each

while read i ; do
  lastlog -u "$i"
done < /root/bin/accountsnames > /root/logs/$(date +%Y-%m-%d).txt
