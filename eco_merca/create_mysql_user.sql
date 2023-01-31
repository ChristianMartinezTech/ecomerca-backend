-- Create ecomerca user
-- Execute this with: sudo mysql -u root -p < create_mysql_user.sql
CREATE USER IF NOT EXISTS 'ecomerca'@'localhost'
    IDENTIFIED BY 'Ecomerca#123';
GRANT ALL PRIVILEGES ON *.* TO 'ecomerca'@'localhost';
FLUSH PRIVILEGES;
