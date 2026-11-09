# Frequency Counter: Given a string `"programming"`, create a dictionary that counts how many times each character appears.


word = "programming"

count = {}

for i in word:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)
