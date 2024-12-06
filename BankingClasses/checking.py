# Import the BankAccount class
from .banking import BankAccount

class CheckingAccount(BankAccount):
    """
    A class representing a checking account.

    Attributes:
        overdraft_limit (float): The maximum negative balance allowed for the account.
        balance (float): The current balance of the account.

    Methods:
        __init__(balance=0, overdraft_limit=100): Initializes a new instance of the CheckingAccount class.
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account.
        get_balance(): Returns the current balance of the account.
    """

    def __init__(self, balance=0, overdraft_limit=100):
        """
        Initializes a new instance of the CheckingAccount class.

        Args:
            balance (float): The initial balance of the account.
            overdraft_limit (float): The maximum negative balance allowed for the account.
        """
        super().__init__(balance)  # Call the parent class constructor to initialize the balance.
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the specified amount exceeds the balance plus overdraft limit.
        """
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds, overdraft limit reached.")

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance
