class User:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    # Getters
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    # Setters
    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password