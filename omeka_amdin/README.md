# Creating users in Omeka

Date: Wed Oct  6 10:14:02 AM EDT 2021
Author: sean

Problem: The SISED server doesn't have an email setup, but the Omeka installation requires an email set up for creating new accounts. In order to create accounts, my solution was to modify the Omeka MySQL database directly:

1. Remove content from the prior semester, including contributor role accounts.
    * Use: ``clean_omeka.sql`` on the remote server
2. Generate the ``roster.sql`` script that creates, defines, and activates the user accounts.
3. Generate the ``omeka_passes.sql`` script that updates the MySQL table user passwords.
4. Generate the ``salts.sql`` script that updates the table with the salts for the user passwords.
    * Use: ``roster2sql.sh`` and send SQL scripts to remote server
5. If requested by the instructor of the course, batch email the temporary passwords to users.
    * Use: ``email_passes.sh``


## Import into MySQL

Example usage:

```
$ mysql -u database_name -p
mysql> use lis602_omeka;
mysql> source roster.sql
```

## Bugs / TODO

1. For multiple sections, need to adjust ID number sequence to avoid redundant ID generation
2. Emails and usernames are missing quotes around those fields in the roster.sql file
