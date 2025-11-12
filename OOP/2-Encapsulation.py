class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # Private attribute (cannot be accessed directly)

    def deposit(self, amount):
        self.__balance += amount # Modify the private value safely

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance # Public method to access private data

account = BankAccount("Bob", "100")
print(account.name)
# print(acc.__balance)    # ❌ Error: 'BankAccount' object has no attribute '__balance'
print(account.get_balance())