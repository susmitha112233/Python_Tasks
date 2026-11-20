"""1. Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details."""

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(self.name, self.roll, self.marks)

s1 = Student("Rahul", 101, 85)
s2 = Student("Anita", 102, 90)
s3 = Student("Ravi", 103, 75)

s1.display()
s2.display()
s3.display()
