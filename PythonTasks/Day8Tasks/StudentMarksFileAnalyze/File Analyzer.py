"""4. Student Marks File Analyzer
A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class"""

f = open("marks.txt", "r")

data = f.readlines()
f.close()

total = 0
count = 0

for line in data:
    name, marks = line.split()
    marks = int(marks)

    print(name, marks)

    total = total + marks
    count = count + 1

average = total / count

print("Average marks:", average)
