def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.

    The function prompts the user to select an account and make a withdrawal.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After each withdrawal, the function prints the updated balance of the respective account.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to make a withdrawal?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("Enter 'q' to quit.")

    # Prompt user to select an account or quit
    choice = input("Select an account to withdraw from (1 or 2): ").strip().lower()

    if choice == 'q':
        print("Withdrawal process canceled.")
        return

    try:
        if choice in ['1', '2']:
            try:
                # Prompt for withdrawal amount
                amount = float(input("Enter the amount to withdraw: ").strip())
                if amount <= 0:
                    raise ValueError("The withdrawal amount must be greater than zero.")

                if choice == '1':
                    # Withdraw from checking account
                    if checking.get_balance() >= amount:
                        checking.withdraw(amount)
                        print(f"Withdrawal successful. Checking account balance: ${checking.get_balance():,.2f}")
                    else:
                        print("Insufficient funds in Checking Account.")
                elif choice == '2':
                    # Withdraw from savings account
                    if savings.get_balance() >= amount:
                        savings.withdraw(amount)
                        print(f"Withdrawal successful. Savings account balance: ${savings.get_balance():,.2f}")
                    else:
                        print("Insufficient funds in Savings Account.")
            except ValueError as ve:
                print(f"Invalid amount: {ve}")
                print("Please try again.")
                handle_withdrawal(checking, savings)  # Recursive call for invalid amount
                return
        else:
            raise ValueError("Invalid choice. Please select '1' or '2'.")
    except ValueError as ve:
        print(ve)
        print("Please try again.")
        handle_withdrawal(checking, savings)  # Recursive call for invalid choice
