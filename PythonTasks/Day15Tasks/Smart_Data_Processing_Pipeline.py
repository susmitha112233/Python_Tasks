"""9. Smart Data Processing Pipeline
Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time"""

import numpy as np
import pandas as pd
import time

# Create numbers.txt automatically
f = open("numbers.txt", "w")
f.write("10\n20\n30\n40\n50\n")
f.close()

# Decorator to calculate execution time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

# Generator to read numbers
def read_numbers():
    f = open("numbers.txt", "r")

    for line in f:
        try:
            yield float(line.strip())
        except ValueError:
            print("Invalid data:", line)

    f.close()

# Process data
@timer
def process():
    numbers = list(read_numbers())

    arr = np.array(numbers)

    print("Numbers:", arr)
    print("Mean:", np.mean(arr))
    print("Standard deviation:", np.std(arr))

    df = pd.DataFrame(arr, columns=["Numbers"])
    print(df)

process()
