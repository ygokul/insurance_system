class User:
    def __init__(self, userId=None, username=None, password=None, role=None):
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    # Getters
    def getUserId(self):
        return self.__userId

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getRole(self):
        return self.__role

    # Setters
    def setUserId(self, userId):
        self.__userId = userId

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setRole(self, role):
        self.__role = role

    def __str__(self):
        return f"User [userId={self.__userId}, username={self.__username}, role={self.__role}]"