"""8. Random Number Generator (Generators)
A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated."""

def numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter N: "))

for x in numbers(n):
    print(x)
