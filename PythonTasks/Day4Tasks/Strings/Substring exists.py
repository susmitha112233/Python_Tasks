# Write a program to check whether a substring exists in a string.

s = input("Enter a string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")
