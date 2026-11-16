"""6. Employee Salary Management System
A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file"""



# Create file and store initial employee details
f = open("employees.txt", "a")
f.close()

# Read employee data
f = open("employees.txt", "r")
data = f.readlines()
f.close()

highest = 0
employee = ""

# Display employee details
for line in data:
    name, salary = line.split()
    salary = int(salary)

    print(name, salary)

    if salary > highest:
        highest = salary
        employee = name

# Display highest salary
print("Highest Salary:", highest)
print("Employee:", employee)

# Add new employee
name = input("Enter employee name: ")
salary = input("Enter salary: ")

f = open("employees.txt", "a")
f.write(name + " " + salary + "\n")
f.close()

print("Employee added successfully")
