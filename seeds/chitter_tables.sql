-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq; 
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Create the table without the foreign key first.
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text,
  name text,
  username text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  content text,
  post_date_time timestamp,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- Add any records that are needed for the tests to run
INSERT INTO users (email, password, name, username) VALUES ('user1@emailaddress.com', 'password1!', 'person1', 'username1');
INSERT INTO users (email, password, name, username) VALUES ('user2@emailaddress.com', 'password2!', 'person2', 'username2');
INSERT INTO users (email, password, name, username) VALUES ('user3@emailaddress.com', 'password3!', 'person3', 'username3');
INSERT INTO users (email, password, name, username) VALUES ('user4@emailaddress.com', 'password4!', 'person4', 'username4');
INSERT INTO users (email, password, name, username) VALUES ('user5@emailaddress.com', 'password5!', 'person5', 'username5');

INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 1 contents.', '2000-12-01 12:00:00', 1);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 2 contents.', '2001-12-01 11:00:00', 2);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 3 contents.', '2002-12-01 12:10:00', 3);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 4 contents.', '2000-07-01 12:15:00', 4);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 5 contents.', '1999-01-12 18:00:00', 5);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 6 contents.', '2002-11-01 12:00:00', 5);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 7 contents.', '2000-12-01 16:00:00', 4);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 8 contents.', '2000-12-01 14:00:00', 3);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 9 contents.', '2003-12-22 09:00:00', 2);
INSERT INTO posts (content, post_date_time, user_id) VALUES ('This is post number 10 contents.', '1999-02-25 12:00:00', 1);


