import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.post import Post
from lib.user import User
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# Routes for Chitter Project:
@app.route('/chitter', methods = ['GET'])
def get_chitter_home():
    connection = get_flask_database_connection(app)
    return render_template('homepage/index.html')

@app.route('/chitter/signup', methods = ['GET'])
def get_signup():
    connection = get_flask_database_connection(app)
    return render_template('users/new_user.html')

@app.route('/chitter/signin', methods = ['GET'])
def get_signin():
    connection = get_flask_database_connection(app)
    return render_template('users/sign_in.html')

@app.route('/chitter', methods = ['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    new_user = User(None, email, password, name, username)

    if not new_user.is_valid():
        return render_template('users/new_user.html', user = new_user, errors = new_user.generates_errors()), 400
    
    repository.create(new_user)
    return redirect("/chitter/signin")


@app.route('/chitter/posts', methods = ['GET'])
def get_posts_sorted():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.sort()
    return render_template('posts/index.html', posts=posts)

# GET posts/new
# Returns a form to create a new post
@app.route('/chitter/posts/new', methods = ['GET'])
def get_new_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    return render_template('posts/new.html')

@app.route('/chitter/posts', methods=['POST'])
def create_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    content = request.form['content']
    user_id = request.form['user_id']
    new_post = Post(None, content, user_id)
    print(new_post)

    if not new_post.is_valid():
        return render_template('posts/new.html', post = new_post, errors = new_post.generates_errors()), 400

    repository.create(new_post)
    return redirect("/chitter/posts")

# ----- End of Routes for Chitter Project -----

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
