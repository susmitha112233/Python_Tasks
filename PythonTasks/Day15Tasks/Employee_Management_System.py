"""5. Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = {}

try:
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    emp = Employee(name, salary)
    employees[name] = salary

    f = open("employee.txt", "w")
    f.write(str(employees))
    f.close()

    # Display employees
    for name, salary in employees.items():
        print(name, salary)

except ValueError:
    print("Enter a valid salary")
