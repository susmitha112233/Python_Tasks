"""11. Boolean Masking for Salary Analysis
Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition."""

import numpy as np

salary = np.array([25000, 40000, 15000, 50000, 30000])

result = salary[salary > 30000]

print("Salaries above 30000:", result)
print("Count:", len(result))
