import random

# Function to calculate and display the change in denominations
def dispense_change(change_owed):
    # Convert change owed to cents to avoid floating-point imprecision
    change = round(change_owed * 100)

    # Calculate each denomination
    dollars = change // 100
    change %= 100

    # Calculate number of quarters
    quarters = change // 25
    change %= 25

    # Calculate number of dimes
    dimes = change // 10
    change %= 10

    # Calculate number of nickels
    nickels = change // 5
    change %= 5

    # Calculate number of pennies
    pennies = change

    # Display the change breakdown
    print("Change breakdown:")
    print(f"${dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")

# Main function to drive the program
def main():
    # Ask the user for the total cost owed (instead of generating it randomly)
    total_owed = float(input(" You owe: $"))

    # Prompt user for the cash amount given
    cash_given = float(input("How much cash will you put the self-checkout: $"))

    # Calculate the change
    change_owed = cash_given - total_owed

    # Check if enough cash was provided
    if change_owed < 0:
        print("Insufficient funds provided.")
    else:
        print(f"Change is: ${change_owed:.2f}")
        dispense_change(change_owed)

# Run the main function
if __name__ == "__main__":
    main()

