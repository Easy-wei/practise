INSERT INTO user 
          (host, user, authentication_string, 
           select_priv, insert_priv, update_priv) 
           VALUES ('localhost', 'guest', 
           PASSWORD('guest123'), 'Y', 'Y', 'Y');

#创建用户，下面的管用，上面的莫名有问题
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
ON TUTORIALS.*
TO 'admin'@'localhost'
IDENTIFIED BY 'qidi1234';