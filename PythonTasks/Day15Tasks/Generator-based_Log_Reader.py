"""7. Generator-based Log Reader
Scenario:
A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary"""

# Create sample log file
f = open("logs.txt", "w")
f.write("INFO\nERROR\nINFO\nERROR\nWARNING\n")
f.close()

# Generator
def read_logs():
    f = open("logs.txt", "r")
    for line in f:
        yield line.strip()
    f.close()

counts = {}

# Read and count errors
for log in read_logs():
    if log == "ERROR":
        print("Error found")

    counts[log] = counts.get(log, 0) + 1

print("Log counts:", counts)
