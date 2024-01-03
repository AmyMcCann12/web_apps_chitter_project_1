from lib.user import User
from lib.post import Post

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['email'], row['password'], row['name'], row['username'])
            users.append(user)
        return users
        
    def find(self, user_id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        user = User(row['id'], row['email'], row['password'], row['name'], row['username'])
        return user
    
    def create(self, user):
        self.connection.execute('INSERT INTO users (email, password, name, username) VALUES (%s, %s, %s, %s)', [user.email, user.password, user.name, user.username])
        return None
    
    def delete(self, user_id):
        self.connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None
    
    def find_with_posts(self, user_id):
        posts = []
        rows = self.connection.execute(
            """SELECT 
            posts.id AS post_id, posts.content,
            posts.post_date_time, posts.user_id
            FROM users JOIN posts
            ON users.id = posts.user_id
            WHERE users.id = %s""",
            [user_id])
        for row in rows:
            post = Post(row['post_id'], row['content'], row['post_date_time'], row['user_id'])
            posts.append(post)
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s', [user_id] )
        user = User(rows[0]['id'], rows[0]['email'], rows[0]['password'], rows[0]['name'], rows[0]['username'], posts)
        print(user)
        return user