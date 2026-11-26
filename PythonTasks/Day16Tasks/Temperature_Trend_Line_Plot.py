"""4. Temperature Trend Line Plot
Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

s = pd.Series(temps)

plt.plot(s, marker="o")
plt.title("Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
