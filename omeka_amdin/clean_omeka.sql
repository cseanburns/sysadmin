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
