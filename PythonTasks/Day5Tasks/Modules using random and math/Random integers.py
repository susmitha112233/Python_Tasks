#Write a Python program using the random module to generate 10 random integers


import random
numbers = []
for i in range(10):
    n = random.randint(1, 100)
    numbers.append(n)
print(numbers)
