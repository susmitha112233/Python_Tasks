#Create a Number Guessing Game where:The program generates a random number between 1 and 50 using random.The user has 5 attempts to guess the number.


import random
import math
number = random.randint(1, 50)
for i in range(5):

    guess = int(input("Guess a number: "))

    diff = math.fabs(number - guess)

    print("Difference:", diff)

    if guess == number:
        print("Correct! You won.")
        break
    else:
        print("Wrong guess! Try again.")

else:
    print("Game Over!")
    print("Correct number is:", number)
