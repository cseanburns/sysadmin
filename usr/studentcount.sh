#!/bin/bash

# Date: September 12, 2019

# Get a count of all members of the 'students' group on the server and
# list them

totalstudents=$(grep 'students' /etc/group | sed -e 's/:/\n/g' | sed -e 's/,/\n/g' | wc -l)
echo ""
echo "There are $(($totalstudents - 3)) student accounts."
echo ""
echo "They include the following:"
grep 'students' /etc/group | sed -e 's/:/\n/g' | sed -e 's/,/\n/g' | tail -n"$(($totalstudents - 3))"
echo ""
