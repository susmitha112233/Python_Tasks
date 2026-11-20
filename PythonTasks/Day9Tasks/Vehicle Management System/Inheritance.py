"""5. Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details."""

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

c = Car("BMW", 120)
b = Bike("Honda", 80)

print("Car Details:")
c.display()

print("Bike Details:")
b.display()
