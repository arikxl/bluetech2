class Bank: 

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open ('transactions.txt', 'a') as file:
            file.write(f'{transaction_string} \t\t\t Balance: {self.balance}\n')

    def withdrawal(self, amount):
        try:
            amount= float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance -= amount
            self.log_transaction(f'Withdrew {amount}')
    def deposit(self, amount):
        try:
            amount= float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance += amount
            self.log_transaction(f'Deposit {amount}')
    

account = Bank(50.50)
while True:
    action = input('What kind of action do you want to?')
    if action in ['Deposit', 'Withdraw']:
        if action == 'Withdraw':
            amount = input('How much do you want to withdraw?')
            account.withdrawal(amount)
        else:
            amount = input('How much do you want to deposit?')
            account.deposit(amount)

        print(f'Your balance is: {account.balance}')
    else: 
        print('That is not a valid action')



# account.deposit(10)
# # print(account.balance)
# account.withdrawal (17.50)
# account.withdrawal (3.45)
# print(account.balance)