class User:
    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

