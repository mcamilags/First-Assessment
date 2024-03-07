class User:
    def __init__(self, name, email, id, password, role):
        self._name = name
        self._email = email
        self._id = id
        self._password = password
        self._role = role

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_id(self):
        return self._id

    def get_password(self):
        return self._password

    def get_role(self):
        return self._role

    def __str__(self):
        return f"{self._role.capitalize()}: {self._name}, Email: {self._email}, ID: {self._id}"
