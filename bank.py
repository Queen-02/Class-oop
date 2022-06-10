class Bank:
    accountType = "Saving Account"
    
    def __init__(self, accountNumber, accountName):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
    
    def deposit(self, amount):
        if amount <= 0:
            return f'Deposit amount should be more than zero'
        else:
            self.balance += amount
            self.deposits.append(amount)
            return f'You have deposited this amount {amount}, and your balance is {self.balance}. {self.deposits}'
            
            
    
    def withdraw(self, amount):

        if amount > self.balance:
            return f'Your balance is {amount}, and you cannot withdraw this {self.balance} amount'
        elif amount < 0:
            return f'Amount is negative, and you cannot withdraw'
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            self.transaction_cost = 100
            self.balance -= amount + self.transaction_cost
            return f'You have withdrawn {amount}, and your balance is {self.balance}. {self.withdrawals}'

    def deposit_statement(self):
        for amount in self.deposits:
            print (f"Here is your ministatement: {amount}")

    def withdraw_statement(self):
        for amount in self.withdrawals:
            print (f"Here is your ministatement: {amount}")
    
    def show_balance(self):
        return f'Your current balance is {self.balance}'