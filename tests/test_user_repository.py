from lib.user_repository import UserRepository
from lib.user import User
from lib.post import Post
from datetime import datetime

"""
When we call UserRepository #all
We get a list of User objects
"""
def test_get_all_users(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'user1@emailaddress.com', 'password1!', 'person1', 'username1'),
        User(2, 'user2@emailaddress.com', 'password2!', 'person2', 'username2'),
        User(3, 'user3@emailaddress.com', 'password3!', 'person3', 'username3'),
        User(4, 'user4@emailaddress.com', 'password4!', 'person4', 'username4'),
        User(5, 'user5@emailaddress.com', 'password5!', 'person5', 'username5')
    ]

"""
When we call UserRepository #find
We get a single User object
"""
def test_get_a_single_user(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    user = repository.find(3)
    assert user == User(3, 'user3@emailaddress.com', 'password3!', 'person3', 'username3')


"""
When we call UserRepository #create
We get a new record in the user database
"""
def test_create_a_user(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    repository.create("test@useremail.com", "password!", "test user", "test username")
    users = repository.all()
    assert users == [
        User(1, 'user1@emailaddress.com', 'password1!', 'person1', 'username1'),
        User(2, 'user2@emailaddress.com', 'password2!', 'person2', 'username2'),
        User(3, 'user3@emailaddress.com', 'password3!', 'person3', 'username3'),
        User(4, 'user4@emailaddress.com', 'password4!', 'person4', 'username4'),
        User(5, 'user5@emailaddress.com', 'password5!', 'person5', 'username5'),
        User(6, "test@useremail.com", "password!", "test user", "test username")
    ]

"""
When we call UserRepository #delete
We can remove a user from the database
"""

def test_delete_a_user(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    repository.delete(3)
    users = repository.all()
    assert users == [
        User(1, 'user1@emailaddress.com', 'password1!', 'person1', 'username1'),
        User(2, 'user2@emailaddress.com', 'password2!', 'person2', 'username2'),
        User(4, 'user4@emailaddress.com', 'password4!', 'person4', 'username4'),
        User(5, 'user5@emailaddress.com', 'password5!', 'person5', 'username5')
    ]

"""
When we call UserRepository #find_with_posts
using a user id,
Then we get the user along with a list of their posts
"""
def test_find_with_posts(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    user_with_posts = repository.find_with_posts(2)
    assert user_with_posts == User(
        2, 'user2@emailaddress.com', 'password2!', 'person2', 'username2',[
            Post(2, 'This is post number 2 contents.', datetime(2001,12,1,11,00,00), 2),
            Post(9,'This is post number 9 contents.', datetime(2003,12,22,9,00,00), 2)
        ])

"""
When we call UserRepository #find_with_posts
and there are no posts
Then we still get the user, but the posts attribute is empty
"""

def test_find_with_no_posts(db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    repository = UserRepository(db_connection)
    repository.create("test@useremail.com", "password!", "test user", "test username")
    user_with_posts = repository.find_with_posts(6)
    assert user_with_posts ==  User(6, "test@useremail.com", "password!", "test user", "test username")