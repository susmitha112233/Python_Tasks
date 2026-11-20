"""16. Library Management System (Constructor & Inheritance)
A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def show(self):
        self.display()
        print("File Size:", self.size, "MB")


b = EBook("Python", "Ravi", 5)
b.show()
