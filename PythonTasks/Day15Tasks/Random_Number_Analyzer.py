'''2. Random Number Analyzer
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates'''

import random

numbers = []

# Generate 10 random numbers
for i in range(10):
    numbers.append(random.randint(1, 50))

print("Numbers:", numbers)

even = 0
odd = 0

# Count even and odd
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

# Remove duplicates
unique = set(numbers)
print("Unique numbers:", unique)
