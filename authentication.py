class Authentication:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        return f"User {user.get_name()} registered successfully."

    def login(self, id, password):
        for user in self.users:
            if user.get_id() == id and user.get_password() == password:
                return user
        return None

    def get_students(self):
        return [user for user in self.users if user.get_role() == "student"]

    def get_admins(self):
        return [user for user in self.users if user.get_role() == "admin"]
