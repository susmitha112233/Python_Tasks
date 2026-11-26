"""1. Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file"""

import math

students = [("Ravi", 80), ("Sita", 45), ("Ram", 70)]

# Convert list of tuples into dictionary
data = dict(students)

total = 0
count = 0

# Find students scoring above 50
for name, marks in data.items():
    if marks > 50:
        print(name, marks)
    total += marks
    count += 1

# Calculate average
average = math.fsum(data.values()) / count
print("Average:", average)

# Store results in file
f = open("students.txt", "w")
f.write(str(data))
f.write("\nAverage: " + str(average))
f.close()

print("Data saved successfully")
