"""9. Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details."""

class Staff:
    def __init__(self, name):
        self.name = name

class Professor(Staff):
    def display(self):
        print("Professor:", self.name)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant:", self.name)

class Administrator(Staff):
    def display(self):
        print("Administrator:", self.name)

p = Professor("Ravi")
l = LabAssistant("Sita")
a = Administrator("Arun")

p.display()
l.display()
a.display()
