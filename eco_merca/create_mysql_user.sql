-- Create ecomerca db
USE mysql;
CREATE USER [IF NOT EXISTS] 'miau'@'localhost'
    IDENTIFIED BY 'Ecomerca#123';
CREATE DATABASE [IF NOT EXISTS] ecomercadb;
GRANT ALL PRIVILEGES ON ecomerca.* TO 'ecomerca'@'localhost';
