"""10. Advanced Simulation System
Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistics"""

import random
import numpy as np
import pandas as pd
import math

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

try:
    names = ["Ravi", "Sita", "Ram", "John", "Anu"]

    # Generate random marks
    marks = np.array([random.randint(0, 100) for i in range(5)])

    students = []

    for i in range(5):
        students.append(Student(names[i], marks[i]))

    grades = []

    for m in marks:
        if m >= 90:
            grades.append("A")
        elif m >= 75:
            grades.append("B")
        elif m >= 60:
            grades.append("C")
        elif m >= 40:
            grades.append("D")
        else:
            grades.append("Fail")

    # Create DataFrame
    df = pd.DataFrame({
        "Name": names,
        "Marks": marks,
        "Grade": grades
    })

    print(df)

    # Statistics
    print("Average:", math.fsum(marks) / len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    # Save report
    df.to_csv("exam_report.csv", index=False)
    print("Report saved successfully")

except Exception as e:
    print("Error:", e)
