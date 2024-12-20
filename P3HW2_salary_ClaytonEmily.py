#Emily Clayton
#October 25,2024
#P3HW2_ClaytonEmily.py
# A brief description of the project: This program calculates the gross pay for an employee based on hours worked and pay rate, including overtime calculation.

def main():
    # Step 1: Get employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Step 2: Determine overtime and regular hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0

    # Step 3: Calculate pay
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Step 4: Display results
    print(f"Employee Name: {employee_name}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Overtime Hours: {overtime_hours}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Pay for Regular Hours: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")

# Run the program
if __name__ == "__main__":
    main()
