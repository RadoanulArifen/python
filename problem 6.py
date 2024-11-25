class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Pages:{self.pages}")

class Ebook:
    def __init__(self,title,author,page,file_format):
        super.__init__(title,author,page)
        self.file_format=file_format
    def display(self):
        super().display()
        print(f"File Format: {self.file_format}")

physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
ebook = Ebook("1984", "George Orwell", 328, "PDF")

print("Physical Book Details:")
physical_book.display()
print("\nEbook Details:")
ebook.display()


