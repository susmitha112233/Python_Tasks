#Dictionary Sorting: Given a dictionary: Arrange students according to marks from highest to lowest and print the top two.

students = {
    "Rahul": 85,
    "Chandu": 92,
    "Sony": 78,
    "Sneha": 95
}

result = sorted(students.items(),
                key=lambda x: x[1],
                reverse=True)

print("Sorted marks:")

for name, marks in result:
    print(name, marks)

print("Top two students:")

for name, marks in result[:2]:
    print(name, marks)

