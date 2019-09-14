#!/bin/bash

# Date: September 12, 2019

# Get a count of all members of the 'faculty' group on the server and
# list them

totalfac=$(grep 'faculty' /etc/group | sed -e 's/:/\n/g' | sed -e 's/,/\n/g' | wc -l)
echo ""
echo "There are $(($totalfac - 3)) faculty or staff accounts."
echo ""
echo "They include the following:"
grep 'faculty' /etc/group | sed -e 's/:/\n/g' | sed -e 's/,/\n/g' | tail -n"$(($totalfac - 3))"
echo ""
