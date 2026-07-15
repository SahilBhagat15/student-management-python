-- Create Database
CREATE DATABASE IF NOT EXISTS studentdb;

USE studentdb;

-- Student Table
CREATE TABLE IF NOT EXISTS students
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    roll_no VARCHAR(20) UNIQUE NOT NULL,

    name VARCHAR(100) NOT NULL,

    age INT,

    gender VARCHAR(10),

    branch VARCHAR(50),

    email VARCHAR(100) UNIQUE,

    phone VARCHAR(15),

    cgpa DECIMAL(3,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User Table
CREATE TABLE IF NOT EXISTS users
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) UNIQUE NOT NULL,

    password VARCHAR(100) NOT NULL
);

-- Insert Default Admin
INSERT INTO users(username,password)
VALUES
('admin','admin123');