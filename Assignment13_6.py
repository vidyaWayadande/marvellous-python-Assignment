class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a positive amount from the account if sufficient funds exist."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ₹{self.balance}")

# Example usage
if __name__ == "__main__":
    # Create a BankAccount object
    account = BankAccount(account_number="123456789", holder_name="John Doe", initial_balance=1000.0)

    # Display initial balance
    account.display_balance()

    # Deposit money
    account.deposit(500)

    # Withdraw money
    account.withdraw(200)

    # Display updated balance
    account.display_balance()
