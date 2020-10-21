#!/bin/bash

#=====================================================================
# 
# FILE: mass_email.sh
#
# USAGE: ./mass_email.sh
#       
# DESCRIPTION: Sends emails to a list of recipients in a CSV file (data.csv) 
# the contents of a text file (letter.html). Make sure both CSV file and HTML 
# file are in working directory (currently, the script does not check that they 
# exist).
#
# The data.csv file contains the following elements. The script can easily be 
# adjusted for a different data structure. Current structure:
#
# title,name,email,cc_email
#
# The letter.html file contains matching variables that are parsed w/ the Bash 
# script:
#
# <p>Dear <<name>>,</p>
#
# <p>We are pleased to accept your ...., <<title>>, for .....</p>
#
# REQUIREMENTS: Mutt 1.5.24, SMTP (e.g., msmtp)
#
# BUGS: Does not test for existence of files. Data must be formatted in a 
# specific way.
#
# NOTES: See Content-Type comment below, should work for Mutt 1.5.24, but 
# isn't.
#
#=====================================================================

while read line
do
    title=$(echo $line | awk -F',' '{print $1}')
    name=$(echo $line | awk -F',' '{print $2}')
    email=$(echo $line | awk -F',' '{print $3}')
    CC=$(echo $line | awk -F',' '{print $4}')
    sed -e "s/<<name>>/$name/g" \
        -e "s/<<title>>/$title/g" letter.html \
        | mutt -c $CC -s "$title + Subject Text" \
        -e "set content_type=text/html" $email
        # alternatively:
        # "-e my_hdr Content-Type: text/html" $email
    sleep 1
done < data.csv
