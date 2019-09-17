#!/bin/bash

# Date: September 12, 2019

# Get a count of all members of the 'faculty' group on the server and
# list them

totalfac=$(grep "faculty" /etc/group | sed -e 's/:/\n/g' | tail -n1 | sed -e 's/,/\n/g' | wc -l)
printf "\n"
printf "There are $(($totalfac)) faculty or staff accounts.\n"
printf "\n"
printf "They include the following:\n"
grep "faculty" /etc/group | sed -e 's/:/\n/g' | tail -n1 | sed -e 's/,/\n/g'
printf "\n"
