class bankaccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

account1 = bankaccount("Alice", 1000)
print(account1.account_holder)  # Output: Alice
account1.account_holder = "Bob"
print(account1.account_holder)  # Output: Bob
account1.__balance = 1031

account1.deposit(500)
account1.withdraw(200)
account1.display_balance()