from lib.post import Post
from datetime import datetime

"""
When I create a post
It constructs with
id, content, post_date_time, user_id
"""

def test_post_constructs_with_properties():
    post = Post(1, "Test Content", "2023-12-10 15:30:00", 1)
    assert post.id == 1
    assert post.content == "Test Content"
    assert post.post_date_time == "2023-12-10 15:30:00"
    assert post.user_id == 1

"""
I can format a post
so that it provides a nice string
"""
def test_format_post():
    post = Post(1, "Test Content", "2023-12-10 15:30:00", 1)
    assert str(post) == "Post(1, Test Content, 2023-12-10 15:30:00, 1)"

"""
When I compare to identical posts
they are classed as equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test Content", "2023-12-10 15:30:00", 1)
    post2 = Post(1, "Test Content", "2023-12-10 15:30:00", 1)
    assert post1 == post2

"""
Test post validity
"""
def test_post_isvalid():
    assert Post(1, "", "2023-12-10 15:30:00", 1).is_valid() == False
    assert Post(1, "Test Content", "", 1).is_valid() == False
    assert Post(1, "Test Content", "2023-12-10 15:30:00", "").is_valid() == False
    assert Post(1, None, "2023-12-10 15:30:00", 1).is_valid() == False
    assert Post(1, "Test Content", None, 1).is_valid() == False
    assert Post(1, "Test Content", "2023-12-10 15:30:00", None).is_valid() == False
    assert Post(None, "Test Content", datetime(2023, 12, 10, 15, 30, 00), 1).is_valid() == True

"""
We can generate errors for an invalid post
"""

def test_post_errors(): 
    assert Post(1, "", "2023-12-10 15:30:00", 1).generates_errors() == "Post content can't be blank"
    assert Post(1, "Test Content", "", 1).generates_errors() == "Post date & time can't be blank"
    assert Post(1, "Test Content", "2023-12-10 15:30:00", "").generates_errors() == "User id can't be blank"
    assert Post(1, None, "2023-12-10 15:30:00", 1).generates_errors() == "Post content can't be blank"
    assert Post(1, "Test Content", None, 1).generates_errors() == "Post date & time can't be blank"
    assert Post(1, "Test Content", "2023-12-10 15:30:00", None).generates_errors() == "User id can't be blank"
    assert Post(1, "Test Content", "2023-12-10 15:30:00", 2).generates_errors() == None
    assert Post(1, "", "2023-12-10 15:30:00", None).generates_errors() == "Post content can't be blank\nUser id can't be blank"