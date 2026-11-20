"""17. Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it"""

def bonus(func):
    def wrapper(self):
        salary = func(self)
        salary = salary + 5000
        print("Salary with Bonus:", salary)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def show_salary(self):
        print("Employee Name:", self.name)
        return self.salary


e = Employee("Ravi", 25000)
e.show_salary()
