class Bank:
    accountType = "Saving Account"
    def __init__(self, accountNumber, pin, accountName):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.pin = pin
    