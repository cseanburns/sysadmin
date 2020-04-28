#!/bin/bash

# Office hour script in Bash; also available in Python!

officeday=$(date +%a)
day1="Tue"
day2="Wed"
email="myemail@uky.edu"

/usr/bin/clear
printf "Christopher Sean Burns, PhD\n"
printf "Associate Professor\n"
printf "$email\n"
printf "859-555-0000\n"
printf "\nSpring 2020\n"
 
if [[ "$officeday" = "$day1" ]] ; then
  printf "\nSince today is "$day1", my office hours are 1:00-3:00p.m.\n"
elif [[ "$officeday" = "$day2" ]] ; then
  printf "\nSince today is "$day2", my office hours are 1:00-3:00p.m.\n"
else
  printf "\nSince today is neither "$day1" nor "$day2",\n"
  printf "please knock on door or email me at\n"
  printf ""$email"\n"
  printf "to schedule an appointment.\n"
fi
