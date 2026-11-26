"""4. Basic File Logger
Scenario:
A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling
"""

try:
    f = open("log.txt", "a")

    while True:
        action = input("Enter action (stop to exit): ")

        if action.lower() == "stop":
            break

        f.write(action + "\n")

    f.close()
    print("Logs saved")

except OSError:
    print("File error")
