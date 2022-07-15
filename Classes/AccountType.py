from Study_Classes.Classes.BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def withdraw(self, value):
        if self._balance < value:
            print('Not enough balance in your account.')
            return
        self._balance -= value
        print('Operation successful')
        self.show_balance()


class CheckingAccount(BankAccount):
    def __init__(self, agency, num_acc, balance, limit=1000):
        super().__init__(agency, num_acc, balance)
        self._limit = limit

    def withdraw(self, value):
        if self._balance + self._limit < value:
            print('Not enough balance in your account, it exceeds your limit.')
            return
        self._balance -= value
        print('Operation successful')
        self.show_balance()
