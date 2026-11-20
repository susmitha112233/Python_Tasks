"""15. Infinite Even Number Generator (Generators)
Create a generator function that continuously generates even numbers starting from
2. The program should print the first N even numbers using this generator."""

def even_numbers():
    n = 2
    while True:
        yield n
        n = n + 2

gen = even_numbers()

N = int(input("Enter N: "))

for i in range(N):
    print(next(gen))
