class BankAccount:
    def __init__(self, initial_balance=0):
        # private attribute
        self.__balance = initial_balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount}. Current balance: {self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdraw amount must be positive.")

    # Method to check the balance (read-only access)
    def get_balance(self):
        return self.__balance


# Create an instance of BankAccount with an initial balance
account = BankAccount(100)

# Deposit and Withdraw money
account.deposit(50)    # Depositing 50
account.withdraw(30)   # Withdrawing 30

# Attempt to access the balance directly (this will cause an error)
# print(account.__balance)  # This will give an error because __balance is private

# Accessing balance using the get_balance method (safe)
print("Final balance:", account.get_balance())
