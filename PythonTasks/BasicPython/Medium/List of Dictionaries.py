#List of Dictionaries: Find the highest salary, employees earning above 35,000, average salary, and employee names.

employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# Highest salary
high = max(employees, key=lambda x: x["salary"])
print("Highest salary:", high)

# Salary greater than 35000
print("Employees with salary above 35000:")

for i in employees:
    if i["salary"] > 35000:
        print(i["name"])

# Average salary
total = 0

for i in employees:
    total = total + i["salary"]

average = total / len(employees)

print("Average salary:", average)

# Print only names
names = []

for i in employees:
    names.append(i["name"])

print("Names:", names)
