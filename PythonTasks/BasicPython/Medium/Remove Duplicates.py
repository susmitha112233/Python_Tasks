#Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.



numbers = [1, 2, 3, 2, 4, 1, 5, 3]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)
