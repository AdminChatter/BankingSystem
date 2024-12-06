# Import the BankAccount class
from .banking import BankAccount

class SavingsAccount(BankAccount):
    """
    A class representing a savings account.

    Attributes:
        balance (float): The current balance of the savings account.
        interest_rate (float): The interest rate for the savings account.

    Methods:
        __init__(balance=0, interest_rate=0.01): Initializes a new instance of the SavingsAccount class.
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account.
        apply_interest(): Applies interest to the account balance.
        get_balance(): Returns the current balance of the account.
    """

    def __init__(self, balance=0, interest_rate=0.01):
        """
        Initializes a new instance of the SavingsAccount class.

        Args:
            balance (float): The initial balance of the account.
            interest_rate (float): The interest rate for the savings account. Default is 1% (0.01).
        """
        super().__init__(balance)  # Call the parent class constructor to initialize the balance.
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """
        Deposits the specified amount into the savings account.

        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the savings account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the specified amount exceeds the current balance.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds.")

    def apply_interest(self):
        """
        Applies the interest rate to the current balance and updates it.
        """
        self.balance += self.balance * self.interest_rate

    def get_balance(self):
        """
        Returns the current balance of the savings account.

        Returns:
            float: The current balance of the savings account.
        """
        return self.balance
