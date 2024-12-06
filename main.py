# Import necessary classes and functions
from .BankingClasses.checking import CheckingAccount
from .BankingClasses.savings import SavingsAccount
from .BankingClasses.validation import Validation
from BankingFunctions import balances
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.withdraw import handle_withdrawal
from BankingFunctions.transfer import handle_transfer


def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
          "contain at least one uppercase and lowercase letter,\n"
          "one number, and one of the following special characters: !@#$%^&*.")
    password = input("Enter your password: ")

    # Initialize the attempts variable to 1
    attempts = 1

    # Validate email and password
    while attempts < 3:
        if not Validation.validate_email(email) or not Validation.validate_password(password):
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1
        else:
            break
    else:
        print("Too many invalid attempts. Exiting the program.")
        return

    # Set up accounts with default balances
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # Print account balances
    print("\nWelcome! Here are your account balances:")
    balances(checking_account, savings_account)

    # Banking menu loop
    while True:
        print("\nBanking Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Show Balances")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        # List of valid choices
        valid_choices = ['1', '2', '3', '4', '5']

        if choice in valid_choices:
            if choice == '1':
                handle_deposit(checking_account, savings_account)
            elif choice == '2':
                handle_withdrawal(checking_account, savings_account)
            elif choice == '3':
                handle_transfer(checking_account, savings_account)
            elif choice == '4':
                balances(checking_account, savings_account)
            elif choice == '5':
                print("Thank you for using our banking system. Goodbye!")
                break
        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
