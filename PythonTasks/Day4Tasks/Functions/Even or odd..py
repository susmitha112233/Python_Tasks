#Write a function to check whether a number is even or odd.

def check(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

n = int(input("Enter a number: "))
check(n)
