class Client:
    def __init__(self, clientId=None, clientName=None, contactInfo=None, policy=None):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policy = policy

    # Getters
    def getClientId(self):
        return self.__clientId

    def getClientName(self):
        return self.__clientName

    def getContactInfo(self):
        return self.__contactInfo

    def getPolicy(self):
        return self.__policy

    # Setters
    def setClientId(self, clientId):
        self.__clientId = clientId

    def setClientName(self, clientName):
        self.__clientName = clientName

    def setContactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    def setPolicy(self, policy):
        self.__policy = policy

    def __str__(self):
        return f"Client [clientId={self.__clientId}, clientName={self.__clientName}, contactInfo={self.__contactInfo}, policy={self.__policy}]"