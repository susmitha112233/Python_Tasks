"""3. Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except"""

items = ["Pen", "Book", "Pen", "Bag"]
prices = {"Pen": 10, "Book": 50, "Bag": 200}

# Remove duplicate items
items = list(set(items))
print("Items:", items)

total = 0

try:
    for item in items:
        if item in prices:
            total += prices[item]
        else:
            print("Invalid item:", item)

    print("Total cost:", total)

except Exception as e:
    print("Error:", e)
