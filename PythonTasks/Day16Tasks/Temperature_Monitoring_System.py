"""4. Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

# High and low temperature count
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.figure(figsize=(10, 6))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(days, temps, marker="o")
plt.title("Temperature Trend")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(days, temps)
plt.title("Day-wise Temperature")

# 3. Pie chart
plt.subplot(2, 3, 3)
plt.pie([high, low], labels=["High", "Low"], autopct="%1.1f%%")
plt.title("High vs Low Temperature")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(temps, bins=5)
plt.title("Temperature Distribution")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(temps)), temps)
plt.title("Index vs Temperature")

plt.tight_layout()
plt.show()
