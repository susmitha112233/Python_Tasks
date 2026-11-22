"""10. Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each par"""

import numpy as np

data = np.array([12, 7, 25, 3, 18, 10])

sorted_data = np.sort(data)

parts = np.split(sorted_data, 2)

sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

print("Sorted array:", sorted_data)
print("First part:", parts[0])
print("Second part:", parts[1])
print("Sum of first part:", sum1)
print("Sum of second part:", sum2)
