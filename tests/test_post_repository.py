from lib.post_repository import PostRepository
from lib.post import Post
from datetime import datetime
from lib.user import User

"""
When we call PostRepository #all
We get a list of all Post objects
"""
def test_post_all(db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1,'This is post number 1 contents.', datetime(2000, 12, 1, 12, 00, 00), 1),
        Post(2,'This is post number 2 contents.', datetime(2001,12,1, 11,00,00), 2),
        Post(3,'This is post number 3 contents.', datetime(2002,12,1, 12,10,00), 3),
        Post(4,'This is post number 4 contents.', datetime(2000,7,1, 12,15,00), 4),
        Post(5,'This is post number 5 contents.', datetime(1999,1,12, 18,00,00), 5),
        Post(6,'This is post number 6 contents.', datetime(2002,11,1, 12,00,00), 5),
        Post(7,'This is post number 7 contents.', datetime(2000,12,1, 16,00,00), 4),
        Post(8,'This is post number 8 contents.', datetime(2000,12,1, 14,00,00), 3),
        Post(9,'This is post number 9 contents.', datetime(2003,12,22, 9,00,00), 2),
        Post(10,'This is post number 10 contents.', datetime(1999,2,25, 12,00,00), 1)
    ]

"""
When we call PostRepository #find
We get a single post object
"""
def test_post_find(db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    repository = PostRepository(db_connection)
    post = repository.find(6)
    assert post == Post(6,'This is post number 6 contents.', datetime(2002,11,1, 12,00,00), 5)

"""
When we call PostRepository #create
We create a new post record in the database
"""
def test_post_create(db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    repository = PostRepository(db_connection)
    repository.create('This is a test post','1999-12-31 23:59:59', 3)
    posts = repository.all()
    assert posts == [
        Post(1,'This is post number 1 contents.', datetime(2000, 12, 1, 12, 00, 00), 1),
        Post(2,'This is post number 2 contents.', datetime(2001,12,1, 11,00,00), 2),
        Post(3,'This is post number 3 contents.', datetime(2002,12,1, 12,10,00), 3),
        Post(4,'This is post number 4 contents.', datetime(2000,7,1, 12,15,00), 4),
        Post(5,'This is post number 5 contents.', datetime(1999,1,12, 18,00,00), 5),
        Post(6,'This is post number 6 contents.', datetime(2002,11,1, 12,00,00), 5),
        Post(7,'This is post number 7 contents.', datetime(2000,12,1, 16,00,00), 4),
        Post(8,'This is post number 8 contents.', datetime(2000,12,1, 14,00,00), 3),
        Post(9,'This is post number 9 contents.', datetime(2003,12,22, 9,00,00), 2),
        Post(10,'This is post number 10 contents.', datetime(1999,2,25, 12,00,00), 1),
        Post(11, 'This is a test post', datetime(1999,12,31,23,59,59), 3)
    ]

"""
When we call PostRepository #delete
We remove a post record from the database
"""
def test_post_deletion(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = PostRepository(db_connection)
    repository.delete(4)
    posts = repository.all()
    assert posts == [
        Post(1,'This is post number 1 contents.', datetime(2000, 12, 1, 12, 00, 00), 1),
        Post(2,'This is post number 2 contents.', datetime(2001,12,1, 11,00,00), 2),
        Post(3,'This is post number 3 contents.', datetime(2002,12,1, 12,10,00), 3),
        Post(5,'This is post number 5 contents.', datetime(1999,1,12, 18,00,00), 5),
        Post(6,'This is post number 6 contents.', datetime(2002,11,1, 12,00,00), 5),
        Post(7,'This is post number 7 contents.', datetime(2000,12,1, 16,00,00), 4),
        Post(8,'This is post number 8 contents.', datetime(2000,12,1, 14,00,00), 3),
        Post(9,'This is post number 9 contents.', datetime(2003,12,22, 9,00,00), 2),
        Post(10,'This is post number 10 contents.', datetime(1999,2,25, 12,00,00), 1)
    ]

"""
When we call PostRepository #find_with_user
We can see the post along with the username
"""
def test_posts_find_with_user(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = PostRepository(db_connection)
    post = repository.find_with_user(3)
    assert post == Post(
        3,'This is post number 3 contents.', datetime(2002,12,1, 12,10,00), 3, User(3, 'user3@emailaddress.com', 'password3!', 'person3', 'username3'))

"""
When we call PostRepository #sort
We can see all posts arranged in reverse chronoloical order
"""

def test_posts_sort(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = PostRepository(db_connection)
    ordered_posts = repository.sort()
    assert ordered_posts == [
        Post(9,'This is post number 9 contents.', datetime(2003,12,22, 9,00,00), 2),
        Post(3,'This is post number 3 contents.', datetime(2002,12,1, 12,10,00), 3),
        Post(6,'This is post number 6 contents.', datetime(2002,11,1, 12,00,00), 5),
        Post(2,'This is post number 2 contents.', datetime(2001,12,1, 11,00,00), 2),
        Post(7,'This is post number 7 contents.', datetime(2000,12,1, 16,00,00), 4),
        Post(8,'This is post number 8 contents.', datetime(2000,12,1, 14,00,00), 3),
        Post(1,'This is post number 1 contents.', datetime(2000, 12, 1, 12, 00, 00), 1),
        Post(4,'This is post number 4 contents.', datetime(2000,7,1, 12,15,00), 4),
        Post(10,'This is post number 10 contents.', datetime(1999,2,25, 12,00,00), 1),
        Post(5,'This is post number 5 contents.', datetime(1999,1,12, 18,00,00), 5)
    ]
