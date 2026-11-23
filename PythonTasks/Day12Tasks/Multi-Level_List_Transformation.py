"""6. Multi-Level List Transformation (Advanced List Comprehension)
A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers."""

data = [[1, 2, 3], [4, 5], [6]]

flat = [i for row in data for i in row]

squares = [i**2 for i in flat if i % 2 == 0]

print("Flattened list:", flat)
print("Even number squares:", squares)
