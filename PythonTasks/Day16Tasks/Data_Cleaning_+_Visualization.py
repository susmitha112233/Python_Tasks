"""10. Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s = pd.Series(data)

# Replace missing values with mean
s = s.fillna(s.mean())

print("Cleaned Data:")
print(s)

# Find average
avg = s.mean()

# Filter values greater than average
filtered = s[s > avg]

# Line graph
plt.subplot(1, 2, 1)
plt.plot(s, marker="o")
plt.title("Cleaned Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
