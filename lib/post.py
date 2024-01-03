from datetime import datetime
class Post:
    def __init__(self, id, content, user_id, post_date_time = datetime.now().replace(second = 0, microsecond=0), user = None):
        self.id = id
        self.content = content
        self.post_date_time = post_date_time
        self.user_id = user_id
        self.user = user or []

    def __repr__(self):
        return f"Post({self.id}, {self.content}, {self.user_id}, {self.post_date_time})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        if self.content == "" or self.content == None:
            return False
        if self.user_id == "" or self.user_id == None:
            return False
        return True
    
    def generates_errors(self):
        errors = []
        if self.content == "" or self.content == None:
            errors.append("Post content can't be blank")
        if self.user_id == "" or self.user_id == None:
            errors.append("User id can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)