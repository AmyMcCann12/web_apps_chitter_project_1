
class User:
    def __init__(self, id, email, password, name, username, posts = None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.username = username
        self.posts = posts or []
    
    def __repr__(self):
        if self.posts == []:
            return f"User({self.id}, {self.email}, {self.password}, {self.name}, {self.username})"
        else:
            return f"User({self.id}, {self.email}, {self.password}, {self.name}, {self.username}, {self.posts})"
        
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def password_valid(self):
        if len(self.password) >= 8:
            if "!" in self.password or "@" in self.password or "$" in self.password or "%" in self.password or "&" in self.password:
                return True
        return False
    
    def is_valid(self):
        if self.email == None or self.email == "":
            return False
        if self.name == None or self.name == "":
            return False
        if self.username == None or self.username == "":
            return False
        special_characters = "!@$%&"
        if len(self.password) < 8 or [char for char in self.password if char in special_characters] == []:
            return False
        return True
        
    def generates_errors(self):
        errors = []
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        if self.name == None or self.name == "":
            errors.append("Name can't be blank")
        if self.username == None or self.username == "":
            errors.append("Username can't be blank")
        special_characters = "!@$%&"
        if len(self.password) < 8 or [char for char in self.password if char in special_characters] == []:
            errors.append("Password must be at least 8 characters and contain one of the following special characters: `!`, `@`,`$`, `%` or `&`")
        if len(errors) == 0:
            return None
        else:
            return "\n".join(errors)