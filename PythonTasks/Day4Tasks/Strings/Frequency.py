# Write a program to count the frequency of each character in a string.

s = input("Enter a string: ")
for ch in set(s):
    print(ch, ":", s.count(ch))
