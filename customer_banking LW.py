# Import the create_cd_account and create_savings_account functions
# from savings_account import create_savings_account
# from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # Savings Account
    savings_balance = float(input("Enter savings account balance: "))
    savings_interest_rate = float(input("Enter savings account interest rate (in %): "))
    savings_months = int(input("Enter nunber of months for savings account: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Interest Earned: {savings_interest_earned:.2f}, Updated Balance: {savings_updated_balance:.2f}")

    

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # CD Account
    cd_balance = float(input("Enter CD account balance: "))
    cd_interest_rate = float(input("Enter CD account interest rate (in %): "))
    cd_months = int(input("Enter number of months for CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account - Interest Earned: {cd_interest_earned:.2f}, Updated Blance: {cd_updated_balance:.2f}")
    

if __name__ == "__main__":
    main()
    
