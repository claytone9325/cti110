#Emily Clayton
#Nov.17, 2024
#5PLAB
# This program will stimilate self-checkout machine. A random float value will generated a total amount for the customer purchase. It will prompte the user to put money into the self-checkout machine( as a float), The program should display the amount in the correct denominations of dollars, quarters, dimes and nickels and pennies 

import random

# Function to calculate and display the change in denominations
def dispense_change(change_owed):
    # Convert change owed to cents to avoid floating-point imprecision
    change = round(change_owed * 100)

    # Calculate each denomination
    dollars = change // 100
    change %= 100

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    # Display the change breakdown
    
    print(f"${dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Generate a random total owed between 1.00 and 100.00
    total_owed = round(random.uniform(1.00, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

# Get valid input for the amount of cash the customer will put in
    cash_given = get_positive_float("How much cash will you put in the self-checkout? $")

    # Calculate the change
    change_owed = cash_given - total_owed

    if change_owed < 0:
        print("Insufficient funds provided.")
    else:
        print(f"Change is: ${change_owed:.2f}")
        dispense_change(change_owed)

# Run the main function
if __name__ == "__main__":
    main()
