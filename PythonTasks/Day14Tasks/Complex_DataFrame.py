"""8. Complex DataFrame Transformation
A DataFrame:
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
Scenario:
● Students scoring below 50 failed
Task:
1. Create a column Status ("Pass"/"Fail")
2. Filter only passed students
3. Calculate average marks of passed student"""

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# 1. Create Status column
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("Student Data:")
print(df)

# 2. Filter passed students
passed = df[df["Status"] == "Pass"]
print("\nPassed Students:")
print(passed)

# 3. Calculate average marks of passed students
average = passed["Marks"].mean()
print("\nAverage Marks of Passed Students:", average)
