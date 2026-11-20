"""6. Shape Area Calculator (Polymorphism)
A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects."""

class Circle:
    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)

class Rectangle:
    def area(self):
        l = 10
        b = 5
        print("Rectangle Area:", l * b)

class Triangle:
    def area(self):
        b = 10
        h = 5
        print("Triangle Area:", 0.5 * b * h)

c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()
