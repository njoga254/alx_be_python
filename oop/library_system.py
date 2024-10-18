

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


# Derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # file size in MB

    def __str__(self):
        return f"{super().get_info()}, File Size: {self.file_size}KB"


# Derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count  # number of pages

    def __str__(self):
        return f"{super().get_info()}, Page Count: {self.page_count}"


# Library class (demonstrating composition)
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        # Add a book (Book, EBook, or PrintBook instance) to the collection
        self.books.append(book)

    def list_books(self):
        # Print details of each book in the library
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book.get_info()}")
