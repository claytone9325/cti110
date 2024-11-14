# Emily Clayton
# Oct 12, 2024
# P2HW2
#Get user to input the grades and get the low, high and the average of grades

# User enters grades for each modules
Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

print()

print("----------Results----------")

# Creates a list
GradesForModules = []

# Add grades to the modules
GradesForModules.append(Module1)
GradesForModules.append(Module2)
GradesForModules.append(Module3)
GradesForModules.append(Module4)
GradesForModules.append(Module5)
GradesForModules.append(Module6)
print()

# Displays Lowest  Grade
print(f"{'Lowest Grade:':}  {min(GradesForModules)}")

print()
# Displays Lowest  Grade
print(f"{'Lowest Grade:':}  {min(GradesForModules)}")

# Displays Highest Grade
print(f"{'Highest Grade:':} {max(GradesForModules)}")

# Displays Sum of Grades
print(f"{'Sum of Grades:':} {sum(GradesForModules)}")

# Displays the average
Average = sum(GradesForModules)/len(GradesForModules)
print(f"{'Average:':}       {Average:.2f}")
print()
