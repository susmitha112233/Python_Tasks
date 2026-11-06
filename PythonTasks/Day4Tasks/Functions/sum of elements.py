#Write a function to find the sum of elements in a list using a user-defined function.

def find_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
numbers = [10, 20, 30, 40, 50]
print("Sum of list:", find_sum(numbers))
