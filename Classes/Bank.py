class Bank:
    def __init__(self):
        self._agencies = [1111, 2222, 3333]
        self._accounts = []
        self._clients = []

    def append_account(self, acc):
        self._accounts.append(acc)

    def append_client(self, client):
        self._clients.append(client)

    def authenticate(self, client):
        if client.name not in self._clients:
            print('Error: Client not found in database.')
            return

        if client.acc.num_acc not in self._accounts:
            print('Error: Account not found in database.')
            return

        if client.acc.agency not in self._agencies:
            print('Error: Agency not found in database.')
            return

        return True
