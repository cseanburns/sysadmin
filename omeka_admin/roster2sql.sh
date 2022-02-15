#!/usr/bin/env bash

# Date: Tue Oct  5 10:53:01 PM EDT 2021
# Author: sean
#
# Purpose: Prepare SQL files that will create user accounts along with passwords
# And import them into the Omeka database
# 
# First, export roster.xlsx from myUK and export as CSV
# Save roster.xlsx as a comma separated and quoted text
# Then run the script in the same directory as the file
#
# Caveat: This should be resistant to student name variations, but that may need further
# testing.
# Be sure to inspect SQL files before importing into MySQL

roster="roster.csv"

# Delete first two rows
sed -i '1,2d' "$roster"

# Keep only needed columns:
awk -F',' '{ print $1, $2, tolower($4), tolower($5) }' "$roster" > tmp.file && \
  /usr/bin/mv tmp.file "$roster" 

# add comma after name
## replace the second quote 
sed -i 's/"/,/2' "$roster"
## replace the first quote 
sed -i 's/^"//' "$roster"
## get rid of double spaces, if any
sed -i 's/  / /g' "$roster"

# Rearrange columns:
# email, username, first name last name 
awk '{ print $NF, $(NF - 1), $2, $1 }' "$roster" > tmp.file && \
  /usr/bin/mv tmp.file "$roster"

# Add quotes around fields
sed -i 's/^/"/' "$roster"
sed -i 's/ /","/' "$roster"
sed -i 's/ /","/' "$roster"
sed -i 's/$/"/' "$roster"

# Get total count of users
totalusers=$(wc -l < "$roster")

# Generate user IDs starting at a high number
for i in $(seq "$totalusers") ; do
  echo $((500 + "$i"))
done > userids

# add userids to $roster
paste -d" " userids "$roster" > tmp.file && \
  /usr/bin/mv tmp.file "$roster"
sed -i 's/ /,/' "$roster"

# Add extra active and role columns at the end
for i in $(seq "$totalusers") ; do
  echo '"1","contributor"'
done > roles

# add active and role columsn to end of $roster
paste -d"," "$roster" roles > tmp.file && \
  /usr/bin/mv tmp.file "$roster" && \
  /usr/bin/rm roles 

# replace beginning of line with (
sed -i 's/^/(/' "$roster"

# replace end of each line with ),
sed -i 's/$/),/' "$roster"

# replace comma on last line with semicolon
sed -i '$ s/,$/;/' "$roster"

# remove extra spaces 
sed -i 's/ "/"/g' "$roster"
sed -i 's/" /"/g' "$roster"

# add to top of file
sed -i '1 i\insert into omeka_users(id, email, username, name, active, role) values' "$roster"

mv "$roster" roster.sql

# NEXT ADD HASHES AND SALTS

# Generate salts and passwords for users

## Generate 16 byte salts for each users:
## Example OUTPUT: 1RyZHZgO1zKFOmVA
for i in $(seq "$totalusers") ; do
  < /dev/urandom tr -dc A-Z-a-z-0-9 | head -c16 ; echo
done > salts

# Generate passwords for users:
if ! hash diceware >/dev/null 2>&1 ; then
  echo "diceware not installed. Installing:" >&2
  sudo apt install diceware
fi

for i in $(seq "$totalusers") ; do
  diceware -n3
done > passes

# Add single quotes around salts and passes
sed -i "s/^/'/" salts
sed -i "s/$/'/" salts
sed -i "s/^/'/" passes
sed -i "s/$/'/" passes 

paste -d"," salts passes > omeka_passes.sql

# Create the update statement for the password field
# Example syntax
# update omeka_users set password=sha1(concat('salt','PASSWORD')) where id="userid";
sed -i '1,$ s/^/update omeka_users set password=sha1(concat(/' omeka_passes.sql
sed -i '1,$ s/$/)) where id=/' omeka_passes.sql
paste -d" " omeka_passes.sql userids > tmp.file && \
  /usr/bin/mv tmp.file omeka_passes.sql
sed -i 's/$/;/' omeka_passes.sql

# Create the update statements for the salt field 
# Example syntax
# update omeka_users set salt='1RyZHZgO1zKFOmVA' where id = 359;
sed -i '1,$ s/^/update omeka_users set salt=/' salts
sed -i '1,$ s/$/ where id =/' salts
paste -d" " salts userids > tmp.file && \
  /usr/bin/mv tmp.file salts
sed -i '1,$ s/$/;/' salts
/usr/bin/mv salts salts.sql

/usr/bin/rm userids passes

# Done
echo "Log into the Omeka database,"
echo "Select the appropriate database, and run:"
echo
echo "source roster.sql"
echo "source omeka_passes.sql"
echo "source salts.sql"
