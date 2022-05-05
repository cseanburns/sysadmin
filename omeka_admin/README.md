# Creating users in Omeka

Date: Wed Oct  6 10:14:02 AM EDT 2021
Author: sean

## Problem

The server doesn't have an email setup, but the Omeka installation requires an
email set up for creating new accounts. So in order to create accounts, my
solution was to modify the Omeka MySQL database directly:

## Procedure 

1. Run the ``roster2sql.sh`` Bash script to generate the following three
scripts. Note, this Bash script only generates scripts, it doesn't run them:
    * The ``roster.sql`` script will create, define, and activate the Omeka
      user accounts.
    * The ``omeka_passes.sql`` script will update the MySQL Omeka table user
      passwords.
    * The ``salts.sql`` script will update the Omeka table with the salts for
      the user passwords.
1. Then login to the MySQL prompt, select the Omeka database, and clear out the
database of past users and content with this script:
    * ``clean_omeka.sql``
5. If requested by the instructor of the course, batch email the temporary
passwords to users.
    * Use: ``email_passes.sh``


## Procedure Commands 

Usage: Presume below that the MySQL Omeka database name is *lis602_omeka* and
the MysQL Omeka username is *lis602_omeka*

```
$ ./roster2sql.sh
$ mysql -u lis602_omeka -p
mysql> use lis602_omeka;
mysql> source clean_omeka.sql 
mysql> source roster.sql
mysql> source omeka_passes.sql
mysql> source salts.sql
```

## Bugs / TODO

1. For multiple sections, need to adjust ID number sequence to avoid redundant
   ID generation
2. Emails and usernames are missing quotes around those fields in the
   roster.sql file
