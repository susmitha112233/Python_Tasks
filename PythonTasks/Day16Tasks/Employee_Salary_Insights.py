"""3. Employee Salary Insights
Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)

# Calculate department-wise salary
dept_salary = df.groupby("Department")["Salary"].sum()

plt.figure(figsize=(10, 6))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(salaries, marker="o")
plt.title("Salary Trend")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Department-wise Salary")

# 3. Pie chart
plt.subplot(2, 3, 3)
plt.pie(dept_salary.values,
         labels=dept_salary.index,
         autopct="%1.1f%%")
plt.title("Department Distribution")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(salaries, bins=5)
plt.title("Salary Distribution")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(salaries)), salaries)
plt.title("Index vs Salary")

plt.tight_layout()
plt.show()
