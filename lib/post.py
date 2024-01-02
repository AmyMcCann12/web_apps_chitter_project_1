
class Post:
    def __init__(self, id, content, post_date_time, user_id, user = None):
        self.id = id
        self.content = content
        self.post_date_time = post_date_time
        self.user_id = user_id
        self.user = user or []

    def __repr__(self):
        return f"Post({self.id}, {self.content}, {self.post_date_time}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        if self.content == "" or self.content == None:
            return False
        if self.post_date_time == "" or self.post_date_time == None:
            return False
        if self.user_id == "" or self.user_id == None:
            return False
        return True
    
    def generates_errors(self):
        errors = []
        if self.content == "" or self.content == None:
            errors.append("Post content can't be blank")
        if self.post_date_time == "" or self.post_date_time == None:
            errors.append("Post date & time can't be blank")
        if self.user_id == "" or self.user_id == None:
            errors.append("User id can't be blank")
        if len(errors) == 0:
            return None
        else:
            return "\n".join(errors)