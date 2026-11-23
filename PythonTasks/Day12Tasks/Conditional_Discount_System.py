"""4. Conditional Discount System (List Comprehension)
A shop has prices:
prices = [100, 200, 300, 400]
Scenario:
● Apply a 10% discount only if price > 200.
Task:
● Use list comprehension with condition to create updated price list."""

prices = [100, 200, 300, 400]

new_prices = [i * 0.9 if i > 200 else i for i in prices]

print("Updated prices:", new_prices)
