from playwright.sync_api import Page, expect
from datetime import datetime

# Tests for your routes go here

def test_get_homepage(page,test_web_address, db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    page.goto(f"http://{test_web_address}/chitter")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text('What would you like to do today?')

def test_get_signin(page,test_web_address, db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    page.goto(f"http://{test_web_address}/chitter")
    page.click('text=Sign In')
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text('Please Sign in')

def test_get_signup(page,test_web_address, db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    page.goto(f"http://{test_web_address}/chitter")
    page.click('text=Sign Up')
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text('Set Up New User Account')

def test_create_new_user(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    page.goto(f"http://{test_web_address}/chitter")
    page.click('text=Sign Up')
    page.fill("input[name='name']", 'Test')
    page.fill("input[name='email']", '1234@testemail.com')
    page.fill("input[name='password']", '12345678!')
    page.fill("input[name='username']", 'Test Username')
    page.click('text=Create New User Account')

def test_create_new_user_error(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    page.goto(f"http://{test_web_address}/chitter")
    page.click('text=Sign Up')
    page.click('text=Create New User Account')
    errors = page.locator('.t-errors')
    expect(errors).to_have_text("There were errors with your submission: Email can't be blank, Name can't be blank, Username can't be blank, Password must be at least 8 characters and contain one of the following special characters: `!`, `@`,`$`, `%` or `&`")

def test_get_posts_sorted(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    page.goto(f"http://{test_web_address}/chitter/posts")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        'This is post number 9 contents.',
        'This is post number 3 contents.',
        'This is post number 6 contents.',
        'This is post number 2 contents.',
        'This is post number 7 contents.',
        'This is post number 8 contents.',
        'This is post number 1 contents.',
        'This is post number 4 contents.',
        'This is post number 10 contents.',
        'This is post number 5 contents.'
    ])
    date_tags = page.locator(".t-post-dates")
    expect(date_tags).to_have_text([
        f"Date: {datetime(2003,12,22, 9,00,00)}",
        f"Date: {datetime(2002,12,1, 12,10,00)}",
        f"Date: {datetime(2002,11,1, 12,00,00)}",
        f"Date: {datetime(2001,12,1, 11,00,00)}",        
        f"Date: {datetime(2000,12,1, 16,00,00)}",
        f"Date: {datetime(2000,12,1, 14,00,00)}",
        f"Date: {datetime(2000, 12, 1, 12,00,00)}",
        f"Date: {datetime(2000,7,1, 12,15,00)}",
        f"Date: {datetime(1999,2,25, 12,00,00)}",
        f"Date: {datetime(1999,1,12, 18,00,00)}",
    ])

"""Create new Peep"""
def test_create_peep(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    page.goto(f"http://{test_web_address}/chitter/posts")
    page.click('text=Create New Peep')
    page.fill("input[name='content']", "Test peep contents")
    page.fill("input[name='user_id']", '4')
    page.click("text=Create Peep")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text([
        'Test peep contents',
        'This is post number 9 contents.',
        'This is post number 3 contents.',
        'This is post number 6 contents.',
        'This is post number 2 contents.',
        'This is post number 7 contents.',
        'This is post number 8 contents.',
        'This is post number 1 contents.',
        'This is post number 4 contents.',
        'This is post number 10 contents.',
        'This is post number 5 contents.'
    ])

def test_create_peep_error(page, test_web_address, db_connection):
    db_connection.seed('seeds/chitter_tables.sql')
    page.goto(f"http://{test_web_address}/chitter/posts")
    page.click('text=Create New Peep')
    page.click('text=Create Peep')
    errors = page.locator('.t-errors')
    expect(errors).to_have_text("There were errors with your submission: Post content can't be blank, User id can't be blank")