#!/bin/bash

# Date: September 12, 2019

# Get a count of all members of the 'students' group on the server and
# list them

total_students=$(grep "students" /etc/group | sed -e 's/:/\n/g' | tail -n1 | sed -s 's/,/\n/g' | wc -l)
printf "\nThere are %s student accounts.\n" "$total_students"
printf "\nThey include the following:\n"
printf "\n"
grep "students" /etc/group | sed -e 's/:/\n/g' | tail -n1 | sed -e 's/,/\n/g' | pr -T -3
printf "\n"
