import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository

# Create a new Flask app
app = Flask(__name__)

# Routes for Chitter Project:
@app.route('/posts')
def get_posts_sorted():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.sort()
    return render_template('posts/index.html', posts=posts)


# ----- End of Routes for Chitter Project -----

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
