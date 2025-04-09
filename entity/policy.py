class Policy:
    def __init__(self, policyId=None, policyName=None, coverageDetails=None, premium=None):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__coverageDetails = coverageDetails
        self.__premium = premium

    # Getters
    def getPolicyId(self):
        return self.__policyId

    def getPolicyName(self):
        return self.__policyName

    def getCoverageDetails(self):
        return self.__coverageDetails

    def getPremium(self):
        return self.__premium

    # Setters
    def setPolicyId(self, policyId):
        self.__policyId = policyId

    def setPolicyName(self, policyName):
        self.__policyName = policyName

    def setCoverageDetails(self, coverageDetails):
        self.__coverageDetails = coverageDetails

    def setPremium(self, premium):
        self.__premium = premium

    def __str__(self):
        return f"Policy [policyId={self.__policyId}, policyName={self.__policyName}, coverageDetails={self.__coverageDetails}, premium={self.__premium}]"