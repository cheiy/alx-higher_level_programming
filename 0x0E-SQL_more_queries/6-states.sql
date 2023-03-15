-- Script creates the database hbtn_0d_usa and the table states in the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.states(id INT UNIQUE PRIMARY, name VARCHAR(256));
ALTER TABLE `hbtn_0d_usa`.`states` ALTER COLUMN name DROP DEFAULT;
