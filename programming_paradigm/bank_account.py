class BankAccount:
    def __init__(self, initial_balance=0):
        # Using encapsulation to protect the balance attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposits a positive amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            # Format output to include the dollar sign and two decimal places
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws an amount if there are sufficient funds in the account."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            # Format output to include the dollar sign and two decimal places
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds for withdrawal.")
            return False

    def display_balance(self):
        """Displays the current account balance."""
        # Format the balance to include the dollar sign and two decimal places
        print(f"Current Balance: ${self.__account_balance:.2f}")


