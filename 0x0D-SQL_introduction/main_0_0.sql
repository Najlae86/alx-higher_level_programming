-- Create database 
DROP DATABASE IF EXISTS hbtn_test_db_7;
CREATE DATABASE IF NOT EXISTS hbtn_test_db_7;
USE hbtn_test_db_7;

-- Create table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
