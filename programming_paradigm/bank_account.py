class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__account_balance = initial_balance #encapsulation
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2}")
        else:
            print(f"Amount must be a positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2}")
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: {self.__account_balance:.2f}")

