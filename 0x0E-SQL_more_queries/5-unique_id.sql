-- Script creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
ALTER TABLE unique_id ALTER COLUMN name DROP DEFAULT;
