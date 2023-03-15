-- Creates the table force_name on MySQL server. Db name passed as an argument of
-- the MySQL command.
CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256));
ALTER TABLE force_name ALTER COLUMN name DROP DEFAULT;
