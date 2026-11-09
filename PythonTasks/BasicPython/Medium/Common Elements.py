#Common Elements Using Sets: Given two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

a = set(list1)
b = set(list2)

print("Common:", a & b)

print("Only first list:", a - b)

print("All elements:", a | b)
    
