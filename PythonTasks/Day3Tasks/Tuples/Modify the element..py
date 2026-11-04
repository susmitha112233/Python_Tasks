#7. Write a program to convert a tuple to a list and modify the element.

t = (10, 20, 30, 40, 50)

lst = list(t)
lst[1] = 100

print("Modified list:", lst)
