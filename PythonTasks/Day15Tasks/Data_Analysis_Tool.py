"""6. Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results"""

import numpy as np
import pandas as pd

names = ["Ravi", "Sita", "Ram", "John"]

# Generate marks
marks = np.random.randint(30, 100, 4)

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print(df)

# Filter passing students
passed = df[df["Marks"] >= 40]
print("Passed students:")
print(passed)

# Calculate average
print("Mean marks:", np.mean(marks))

# Print using loop
for i in range(len(df)):
    print(df["Name"][i], df["Marks"][i])
