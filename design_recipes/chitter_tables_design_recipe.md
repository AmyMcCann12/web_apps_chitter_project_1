# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
```

```
Nouns:
user: email, password, name, username
posts: content, post_date_time, user_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record        | Properties                       |
| ------------- | -------------------------------- |
| users         | email, password, name, username  | 
| post          | content, post_date_time, user_id |

1. Name of the first table (always plural): `users` 

    Column names: `email`, `password`, `name`, `username`

2. Name of the second table (always plural): `posts` 

    Column names: `content`, `post_date_time`, `user_id`

## 3. Decide the column types

```
# EXAMPLE:

Table: users
id: SERIAL
email: text
password: text
name: text
username: text

Table: posts
id: SERIAL
content: text
post_date_time: timestamp
user_id: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> An user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.

## 5. Write the SQL

```sql
-- file: chitter_tables.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  password text,
  name text,
  username text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  content text,
  post_date_time datetime,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 chitter < chitter_tables.sql
```