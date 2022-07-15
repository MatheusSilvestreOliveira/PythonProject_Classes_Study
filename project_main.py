from Classes.Bank import Bank
from Classes.Client import Client
from Classes.AccountType import SavingsAccount, CheckingAccount

bank = Bank()

account_1 = SavingsAccount(1111, 1234, 2000)
account_2 = SavingsAccount(2222, 5678, 500)
account_3 = CheckingAccount(3333, 9012, 3000)
account_4 = CheckingAccount(4444, 3456, 200, 100)

client_1 = Client('Matthew', 24, account_1)
client_2 = Client('Jane', 30, account_2)
client_3 = Client('Rick', 34, account_3)
client_4 = Client('Lary', 28, account_4)

bank.append_account(account_1.num_acc)
bank.append_account(account_2.num_acc)
bank.append_account(account_3.num_acc)
bank.append_account(account_4.num_acc)


bank.append_client(client_1.name)
bank.append_client(client_2.name)
bank.append_client(client_3.name)
bank.append_client(client_4.name)

print('Welcome to the bank, select the number corresponding to your account:\n'
      f'[1] Name: {client_1.name} - Account number: {account_1.num_acc}\n'
      f'[2] Name: {client_2.name} - Account number: {account_2.num_acc}\n'
      f'[3] Name: {client_3.name} - Account number: {account_3.num_acc}\n'
      f'[4] Name: {client_4.name} - Account number: {account_4.num_acc}')
inp = input('Input: ')
client = None

if inp == '1':
    client = client_1
elif inp == '2':
    client = client_2
elif inp == '3':
    client = client_3
elif inp == '4':
    client = client_4
else:
    print('Invalid input')

inp = None
if client:
    if bank.authenticate(client):
        print('\n#########################################\n')
        print(f'{client.name} / Ag - {client.acc.agency}  Acc - {client.acc.num_acc}\n'
              f'Operations:\n'
              f'[1] Deposit\n'
              f'[2] Withdraw')
        inp = input('Input: ')

        if inp == '1':
            if bank.authenticate(client):
                value = float(input('Deposit value: '))
                client.acc.deposit(value)
        elif inp == '2':
            if bank.authenticate(client):
                value = float(input('Withdraw value: '))
                client.acc.withdraw(value)
        else:
            print('Invalid input')
