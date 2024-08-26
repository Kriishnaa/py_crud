CREATE DATABASE test_db;

USE test_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(255) NOT NULL
);
