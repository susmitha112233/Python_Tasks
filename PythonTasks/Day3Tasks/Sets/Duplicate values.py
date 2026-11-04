#Write a program to remove duplicate values from a list using a set.

numbers = [10, 20, 30, 20, 40, 10, 50]

unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
