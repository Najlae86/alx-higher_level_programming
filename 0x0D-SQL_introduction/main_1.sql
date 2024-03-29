-- Create database
DROP DATABASE IF EXISTS hbtn_test_db_16;
CREATE DATABASE IF NOT EXISTS hbtn_test_db_16;
USE hbtn_test_db_16;

-- Create table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Create records
INSERT INTO second_table (id, score) VALUES (1, 12);
INSERT INTO second_table (id, name, score) VALUES (2, "B", 2);
INSERT INTO second_table (id, name, score) VALUES (3, "C", -12);
INSERT INTO second_table (id, score) VALUES (4, 89);
INSERT INTO second_table (id, name, score) VALUES (5, "E", 0);
INSERT INTO second_table (id, name, score) VALUES (6, "F", 23);
INSERT INTO second_table (id, score) VALUES (7, 5);
INSERT INTO second_table (id, name, score) VALUES (8, "H", 6);
INSERT INTO second_table (id, score) VALUES (9, -9);
INSERT INTO second_table (id, name, score) VALUES (10, "J", 3);
