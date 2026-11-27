"""5. Product Sales & Profit Analysis
Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

plt.figure(figsize=(10, 6))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(products, sales, marker="o")
plt.title("Sales Trend")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(products, sales)
plt.title("Product Sales")

# 3. Pie chart
plt.subplot(2, 3, 3)
plt.pie(sales, labels=products, autopct="%1.1f%%")
plt.title("Sales Contribution")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(profit, bins=5)
plt.title("Profit Distribution")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(sales, profit)
plt.title("Sales vs Profit")

plt.tight_layout()
plt.show()
