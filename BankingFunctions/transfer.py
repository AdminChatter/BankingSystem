def handle_transfer(checking, savings):
    """
    Handles the transfer of funds between checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.

    The function prompts the user to select an account to make a transfer.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After the transfer, the function prints the updated balances of both accounts.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to transfer from?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("Enter 'q' to quit.")

    # Prompt user to select an account or quit
    choice = input("Select an account to transfer from (1 or 2): ").strip().lower()

    if choice == 'q':
        print("Transfer process canceled.")
        return

    try:
        if choice in ['1', '2']:
            try:
                # Prompt the user to enter the amount to transfer
                amount = float(input("Enter the amount to transfer: ").strip())
                if amount <= 0:
                    raise ValueError("The transfer amount must be greater than zero.")

                if choice == '1':
                    # Transfer from checking to savings
                    if checking.get_balance() >= amount:
                        checking.withdraw(amount)
                        savings.deposit(amount)
                        print(f"Transfer successful! ${amount:,.2f} transferred from Checking to Savings.")
                    else:
                        print("Insufficient funds in Checking Account.")
                elif choice == '2':
                    # Transfer from savings to checking
                    if savings.get_balance() >= amount:
                        savings.withdraw(amount)
                        checking.deposit(amount)
                        print(f"Transfer successful! ${amount:,.2f} transferred from Savings to Checking.")
                    else:
                        print("Insufficient funds in Savings Account.")
                
                # Display updated balances
                balances(checking, savings)
            except ValueError as ve:
                print(f"Invalid amount: {ve}")
                print("Please try again.")
                handle_transfer(checking, savings)  # Recursive call for invalid amount
                return
        else:
            raise ValueError("Invalid choice. Please select '1' or '2'.")
    except ValueError as ve:
        print(ve)
        print("Please try again.")
        handle_transfer(checking, savings)  # Recursive call for invalid choice

def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings: ${savings.get_balance():,.2f}")
