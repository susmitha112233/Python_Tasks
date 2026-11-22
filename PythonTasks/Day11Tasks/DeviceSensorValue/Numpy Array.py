"""2. Device Sensor Value (Scalar Array)
An IoT device records a single sensor reading = 75.
Task:
● Create a 0-D NumPy array with this value.
● Print the value and check its number of dimension"""

import numpy as np

value = np.array(75)

print("Value:", value)
print("Dimensions:", value.ndim)
