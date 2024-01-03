from playwright.sync_api import Page, expect
from datetime import datetime

# Tests for your routes go here

def test_get_posts_sorted(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter_tables.sql")
    page.goto(f"http://{test_web_address}/posts")
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
    page.goto(f"http://{test_web_address}/posts")
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