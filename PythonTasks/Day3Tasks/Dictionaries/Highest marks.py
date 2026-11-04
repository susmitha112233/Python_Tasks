#Write a program to find the student with the highest marks from a dictionary.

students = {
    "Chandu": 85,
    "Sony": 90,
    "Ramya": 78
}

topper = max(students, key=students.get)

print("Student with highest marks:", topper)
print("Highest Marks:", students[topper])
