#Emily Clayton
#October 19,2024
#P3HW_1ClaytonEmily.py
#Fix the coding errors in the program


# This program takes a number grade, determines average, and displays letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)
print()


print('----------Results--------')
print(f'Lowest grade: {low}')
print(f'Highest grade: {high}')
print(f'Your total sum of grades is: {total_sum}')
print(f'Average grade: {avg:.2f}')
print('-------------------------')

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
else:
    print('Your grade is: F')

