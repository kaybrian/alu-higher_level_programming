-- create use if not there 
CREATE USER IF NOT EXISTS 'new_user_0d_1user'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
