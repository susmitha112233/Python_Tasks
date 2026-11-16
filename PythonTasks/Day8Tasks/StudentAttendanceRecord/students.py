#A teacher wants to store student attendance in a file named attendance.txt. Write aPython program that takes a student name as input and appends it to the file. Then
#display the contents of the file.


file=open("attendance.txt","a")
c=str(input("enter the name"))
file.write(c +"\n")
file.close()
file=open("attendance.txt","r")
print(file.read())
file.close()


