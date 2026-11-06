#Write a program using a user-defined function to add two numbers.

def add(a, b):
    return a + b
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum =", add(x, y))
