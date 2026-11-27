"""1. Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# Pass and Fail count
pass_count = np.sum(marks > 50)
fail_count = np.sum(marks <= 50)

plt.figure(figsize=(10, 6))

# 1. Line graph
plt.subplot(2, 3, 1)
plt.plot(students, marks, marker="o")
plt.title("Marks Trend")

# 2. Bar chart
plt.subplot(2, 3, 2)
plt.bar(students, marks)
plt.title("Student Marks")

# 3. Pie chart
plt.subplot(2, 3, 3)
plt.pie([pass_count, fail_count],
         labels=["Pass", "Fail"],
         autopct="%1.1f%%")
plt.title("Pass vs Fail")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(marks, bins=5)
plt.title("Marks Distribution")

# 5. Scatter plot
plt.subplot(2, 3, 5)
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")

plt.tight_layout()
plt.show()
