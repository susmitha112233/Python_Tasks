"""12. Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values"""

import numpy as np

arr = np.random.rand(8)

arr = arr * 100

print("Normalized values:", arr)

result = arr[arr > 50]

result = np.sort(result)

print("Values above 50:", result)
