from playwright.sync_api import Page, expect

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