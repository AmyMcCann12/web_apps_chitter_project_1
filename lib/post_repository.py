from lib.post import Post
from lib.user import User
from datetime import datetime

class PostRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            post = Post(row['id'], row['content'], row['user_id'], row['post_date_time'])
            posts.append(post)
        return posts
    
    def find(self, id):
        rows = self.connection.execute('SELECT * FROM posts WHERE id = %s', [id])
        row = rows[0]
        post = Post(row['id'], row['content'], row['user_id'], row['post_date_time'])
        return post
    
    def create(self, post):
        self.connection.execute('INSERT INTO posts (content, post_date_time, user_id) VALUES (%s, %s, %s)', [post.content, post.post_date_time, post.user_id])
        return None 
    
    def delete(self, id):
        self.connection.execute('DELETE FROM posts WHERE id = %s', [id])
    
    def find_with_user(self, post_id):
        users = []
        rows = self.connection.execute(
            """SELECT
            posts.id AS post_id,
            posts.content,
            posts.post_date_time,
            posts.user_id,
            users.email,
            users.password,
            users.name,
            users.username
            FROM posts
            JOIN users
            ON posts.user_id = users.id
            WHERE posts.id = %s""", [post_id]
        )
        row = rows[0]
        user = User(row['user_id'], row['email'], row['password'], row['name'], row['username'])
        post = Post(row['post_id'], row['content'], row['user_id'], row['post_date_time'], user)
        return post
    
    def sort(self):
        posts = self.all()
        ordered_posts = sorted(posts, key=lambda x: x.post_date_time, reverse=True)
        return ordered_posts