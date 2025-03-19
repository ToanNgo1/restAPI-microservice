CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth12';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR (255) NOT NULL UNIQUE,
    password VARCHAR (255) NOT NULL 
);

INSERT INTO user (email, password) VALUE ('nazu_db','nazudb')/* this will run after the above are finish setting up the db and this will be responsible to insert a user in to the tables*/
/* RUN THIS ON CMD 
DROP DATABASE [database name]
DROP USER [user_name]
this use to drop the database and the user from sql*/