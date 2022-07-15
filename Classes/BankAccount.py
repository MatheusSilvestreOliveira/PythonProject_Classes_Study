from abc import abstractmethod, ABC


class BankAccount(ABC):
    def __init__(self, agency, num_acc, balance):
        self._agency = agency
        self._num_acc = num_acc
        self._balance = balance

    def deposit(self, value):
        self._balance += value
        print('Operation successful')
        self.show_balance()

    @property
    def agency(self):
        return self._agency

    @property
    def num_acc(self):
        return self._num_acc

    @abstractmethod
    def withdraw(self, value): pass

    def show_balance(self):
        print(f'Current balance: ${self._balance}')
