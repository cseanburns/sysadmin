/*
Date: Thu May  5 12:42:04 PM EDT 2022

Purpose:
This script removes all past users and content from an Omeka installation.
This script assumes that the Omeka database is named "lis602_omeka".
Feel free to change if the database has a different name by changing
the name in the first line of code below.

To run:
Login to MySQL
Select Omeka Database
Run script at MySQL prompt: source script.sql
*/

use lis602_omeka;
delete from omeka_collections where owner_id > 0;
delete from omeka_files where id > 0;
delete from omeka_items where owner_id > 0;
delete from omeka_records_tags where id > 0;
delete from omeka_search_texts where id > 0;
delete from omeka_sessions where lifetime = 1209600;
delete from omeka_tags where id > 0;
delete from omeka_users where role = "contributor";
delete from omeka_element_texts where id > 0;
