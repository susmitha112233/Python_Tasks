"""5. Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results."""

f = open("article.txt", "r")

data = f.read()
f.close()

words = len(data.split())
lines = len(data.splitlines())
characters = len(data)

print("Words:", words)
print("Lines:", lines)
print("Characters:", characters)
