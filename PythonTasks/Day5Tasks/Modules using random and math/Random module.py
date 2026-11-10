#Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list.

import random
import math
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 200))

print("Numbers:", numbers)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Square Root:", math.sqrt(maximum))
print("Logarithm:", math.log(minimum))
