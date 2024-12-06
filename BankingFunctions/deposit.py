def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("Enter 'q' to quit.")

    # Prompt user to select an account or quit
    choice = input("Select an account (1 or 2): ").strip().lower()

    if choice == 'q':
        print("Deposit process canceled.")
        return

    try:
        if choice in ['1', '2']:
            # Prompt for deposit amount
            try:
                amount = float(input("Enter the amount to deposit: ").strip())
                if amount <= 0:
                    raise ValueError("The deposit amount must be greater than zero.")

                if choice == '1':
                    # Deposit to checking account
                    checking.deposit(amount)
                    print(f"Deposit successful. Checking account balance: ${checking.balance:,.2f}")
                elif choice == '2':
                    # Deposit to savings account
                    savings.deposit(amount)
                    print(f"Deposit successful. Savings account balance: ${savings.balance:,.2f}")

            except ValueError as ve:
                print(f"Invalid amount: {ve}")
                print("Please try again.")
                handle_deposit(checking, savings)  # Recursive call for invalid amount
                return
        else:
            raise ValueError("Invalid choice. Please select '1' or '2'.")
    except ValueError as ve:
        print(ve)
        print("Please try again.")
        handle_deposit(checking, savings)  # Recursive call for invalid choice
