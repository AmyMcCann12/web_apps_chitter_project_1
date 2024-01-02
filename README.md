# Chitter Project

This is a project based on creating a small Twitter clone

## User Stories
There are three stages to the User stories, I will initially work on the project to set up Part 1, then progress onto Part 2 and Part 3.

### Part 1:
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

### Part 2:
As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

### Part 3:
As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep

## Set-up:
```shell
# Clone the repository to your local machine
; git clone TBC YOUR_PROJECT_NAME

# Enter your directory
; cd YOUR_PROJECT_DIRECTORY

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser to use for testing
; playwright install

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit TBC in your browser
```

