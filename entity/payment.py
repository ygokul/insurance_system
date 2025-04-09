class Payment:
    def __init__(self, paymentId=None, paymentDate=None, paymentAmount=None, client=None):
        self.__paymentId = paymentId
        self.__paymentDate = paymentDate
        self.__paymentAmount = paymentAmount
        self.__client = client

    # Getters
    def getPaymentId(self):
        return self.__paymentId

    def getPaymentDate(self):
        return self.__paymentDate

    def getPaymentAmount(self):
        return self.__paymentAmount

    def getClient(self):
        return self.__client

    # Setters
    def setPaymentId(self, paymentId):
        self.__paymentId = paymentId

    def setPaymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    def setPaymentAmount(self, paymentAmount):
        self.__paymentAmount = paymentAmount

    def setClient(self, client):
        self.__client = client

    def __str__(self):
        return f"Payment [paymentId={self.__paymentId}, paymentDate={self.__paymentDate}, paymentAmount={self.__paymentAmount}, client={self.__client}]"