class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred: {amount} to account {target_account.account_number}.")
        else:
            print("Insufficient funds or invalid transfer amount.")
            
account1 = BankAccount("123456", 1000)
account2 = BankAccount("654321", 0)

# account1.deposit(200)
# account1.withdraw(150)
print("Account 1 balance:", account1.get_balance())

account1.transfer(300, account2)
print("Account 1 balance after transfer:", account1.get_balance())
print("Account 2 balance after receiving transfer:", account2.get_balance())