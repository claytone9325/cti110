#Emily Clayton
#Nov. 9, 2024
#P4HW2_Salary
#Calculate salary

#Program will take input and calculate and display nicely. 

# Initialize variables for totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0

# Main loop to input employee data
while True:
    # Input employee's name
    employee_name = input("Enter employee's name ('Done' to exit): ").strip()
    
    if employee_name.lower() == 'done':
        break
    
    # Input number of hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? $"))
    
    # Calculate regular and overtime pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
    
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    
    # Print employee details
    print('-' * 75)
    print(f"Employee name: {employee_name}")
    print('-' * 75)

    # Display the table header
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime Hours':<18}{'Overtime Pay':<18}{'Regular Pay':<18}{'Gross Pay':<18}")
    print('-' * 75)
    
    # Display the employee data
    print(f"{hours_worked:<15.1f}{pay_rate:<15.2f}{overtime_hours:<18.1f}${overtime_pay:>17.2f}${regular_pay:>16.2f}${gross_pay:>16.2f}")
    print('-' * 75)

# Display the overall totals
print('\n' + '=' * 75)
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
print('=' * 75)


    
    
    
