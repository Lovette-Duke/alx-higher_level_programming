-- creates user with all privilages

CREATE USER IF NOT EXISTS 'user_do_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;
FLUSH PRIVILAGES;