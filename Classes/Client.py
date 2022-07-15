from Study_Classes.Classes.Person import Person


class Client(Person):
    def __init__(self, name, age, acc):
        super().__init__(name, age)
        self._acc = acc

    @property
    def acc(self):
        return self._acc
