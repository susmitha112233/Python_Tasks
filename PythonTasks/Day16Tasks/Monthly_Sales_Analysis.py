"""2. Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

plt.figure(figsize=(10, 6))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(months, sales, marker="o")
plt.title("Sales Trend")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(months, sales)
plt.title("Month-wise Sales")

# 3. Pie chart
plt.subplot(2, 3, 3)
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Sales Contribution")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(sales, bins=5)
plt.title("Sales Distribution")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(sales)), sales)
plt.title("Index vs Sales")

plt.tight_layout()
plt.show()
