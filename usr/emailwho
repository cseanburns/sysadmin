#!/bin/bash

# Search email addresses to get user account for specific person
# Date: Thu Sep 12 15:24:07 EDT 2019

# To use:
# s-nail -s "subject message" $(emailwho.sh [grep string])
# Because of the awk command, assumes a file structured like:
# "last name, first name","username",...

lookup="addresses.csv"

grep -i "$1" "$lookup" | awk -F, '{ print $3}' | sed 's/"//g'
