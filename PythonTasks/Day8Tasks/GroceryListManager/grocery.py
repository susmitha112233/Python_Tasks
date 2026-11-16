"""3. Grocery List Manager
A user wants to save grocery items in a file grocery.txt. Write a Python program that takes multiple items from the user and writes them into the file, with each item on a
new line"""

f = open("grocery.txt", "w")

while True:
    item = input("Enter item (stop to finish): ")

    if item == "stop":
        break

    f.write(item + "\n")

f.close()

print("Items saved successfully")
