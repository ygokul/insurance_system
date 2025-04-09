class Claim:
    def __init__(self, claimId=None, claimNumber=None, dateFiled=None, claimAmount=None, status=None, policy=None, client=None):
        self.__claimId = claimId
        self.__claimNumber = claimNumber
        self.__dateFiled = dateFiled
        self.__claimAmount = claimAmount
        self.__status = status
        self.__policy = policy
        self.__client = client

    # Getters
    def getClaimId(self):
        return self.__claimId

    def getClaimNumber(self):
        return self.__claimNumber

    def getDateFiled(self):
        return self.__dateFiled

    def getClaimAmount(self):
        return self.__claimAmount

    def getStatus(self):
        return self.__status

    def getPolicy(self):
        return self.__policy

    def getClient(self):
        return self.__client

    # Setters
    def setClaimId(self, claimId):
        self.__claimId = claimId

    def setClaimNumber(self, claimNumber):
        self.__claimNumber = claimNumber

    def setDateFiled(self, dateFiled):
        self.__dateFiled = dateFiled

    def setClaimAmount(self, claimAmount):
        self.__claimAmount = claimAmount

    def setStatus(self, status):
        self.__status = status

    def setPolicy(self, policy):
        self.__policy = policy

    def setClient(self, client):
        self.__client = client

    def __str__(self):
        return f"Claim [claimId={self.__claimId}, claimNumber={self.__claimNumber}, dateFiled={self.__dateFiled}, claimAmount={self.__claimAmount}, status={self.__status}, policy={self.__policy}, client={self.__client}]"