"""9. Combined Visualization Dashboard
Scenario:
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
Task:
● Create DataFrame
● Plot:
○ Line graph (trend)
○ Bar chart (comparison)
○ Pie chart (distribution)
● Show all in single figure (subplots)"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# Line graph
ax[0].plot(df["Product"], df["Sales"], marker="o")
ax[0].set_title("Line Graph")

# Bar chart
ax[1].bar(df["Product"], df["Sales"])
ax[1].set_title("Bar Chart")

# Pie chart
ax[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
ax[2].set_title("Pie Chart")

plt.tight_layout()
plt.show()
