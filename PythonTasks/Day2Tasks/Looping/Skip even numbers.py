#5. Print numbers from 1 to 10 but skip even numbers using continue.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
