from lib.user import User

"""
When I create a user
It constructs with
id, email, password, name, username
"""

def test_user_constructs_with_properties():
    user = User(1, "user@testemail.com", "password123!", "Test Name", 'Username')
    assert user.id == 1
    assert user.email == "user@testemail.com"
    assert user.password == "password123!"
    assert user.name == "Test Name"
    assert user.username == "Username"

"""
I can format a user 
so that it provides a nice string
"""
def test_users_format_nicely():
    user = User(1, "user@testemail.com", "password123!", "Test Name", 'Username')
    assert str(user) == "User(1, user@testemail.com, password123!, Test Name, Username)"

"""
When I compare two identical users
they are classed as equal
"""
def test_users_are_equal():
    user1 = User(1, "user@testemail.com", "password123!", "Test Name", 'Username')
    user2 = User(1, "user@testemail.com", "password123!", "Test Name", 'Username')
    assert user1 == user2
"""
Test password for validity:
minimum 8 characters and must contain a special character
"""
def test_user_password_isvalid():
    assert User(1, "user@testemail.com", "password", "Test Name", 'Username').is_valid() == False
    assert User(1, "user@testemail.com", "1234567", "Test Name", 'Username').is_valid() == False
    assert User(1, "user@testemail.com", "password!", "Test Name", 'Username').is_valid() == True
    assert User(1, "user@testemail.com", "password?", "Test Name", 'Username').is_valid() == False
    assert User(1, "user@testemail.com", "password@", "Test Name", 'Username').is_valid() == True
    assert User(1, "user@testemail.com", "password$", "Test Name", 'Username').is_valid() == True
    assert User(1, "user@testemail.com", "password%", "Test Name", 'Username').is_valid() == True
    assert User(1, "user@testemail.com", "password&", "Test Name", 'Username').is_valid() == True
    assert User(1, "user@testemail.com", "1234&$!", "Test Name", 'Username').is_valid() == False

"""
Test user validity
"""
def test_user_isvalid():
    assert User(1, "", "password!", "", "").is_valid() == False
    assert User(1, "user@testemail.com", "password!", "Test Name", "").is_valid() == False
    assert User(1, "user@testemail.com", "password!", "", "Username").is_valid() == False
    assert User(1, "", "password!", "Test Name", "Usernme").is_valid() == False
    assert User(1, "user@testemail.com", "password!", "Test Name", None).is_valid() == False
    assert User(1, "user@testemail.com", "password!", None, "Username").is_valid() == False
    assert User(1, None, "password!", "Test Name", "Usernme").is_valid() == False
    assert User(None, "user@testemail.com", "password!", "Test Name", "Usernme").is_valid() == True

"""
We can generate errors for an invalid user
"""
def test_user_errors():
    assert User(1, "", "password!", "", "").generates_errors() == "Email can't be blank, Name can't be blank, Username can't be blank"
    assert User(1, "user@testemail.com", "password!", "Test Name", "").generates_errors() == "Username can't be blank"
    assert User(1, "user@testemail.com", "password!", "", "Username").generates_errors() == "Name can't be blank"
    assert User(1, "", "password!", "Test Name", "Usernme").generates_errors() == "Email can't be blank"
    assert User(1, "user@testemail.com", "password!", "Test Name", None).generates_errors() == "Username can't be blank"
    assert User(1, "user@testemail.com", "password!", None, "Username").generates_errors() == "Name can't be blank"
    assert User(1, None, "password!", "Test Name", "Usernme").generates_errors() == "Email can't be blank"
    assert User(None, "user@testemail.com", "password!", "Test Name", "Usernme").generates_errors() == None
    assert User(1, "user@testemail.com", "pass?", "Test Name", 'Username').generates_errors() == """Password must be at least 8 characters and contain one of the following special characters: `!`, `@`,`$`, `%` or `&`"""
    assert User(1, "", "pass?", "Test Name", 'Username').generates_errors() == """Email can't be blank, Password must be at least 8 characters and contain one of the following special characters: `!`, `@`,`$`, `%` or `&`"""