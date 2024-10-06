class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' is already available.")

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of a book."""
        status = "Available" if not self._is_checked_out else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    """Class representing a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private attribute to store the list of books

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"'{book.title}' by {book.author} has been added to the library.")
        else:
            print("Only instances of Book can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"'{title}' is currently checked out.")
                return
        print(f"No book with the title '{title}' found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                else:
                    print(f"'{title}' is not currently checked out.")
                return
        print(f"No book with the title '{title}' found in the library.")

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available for checkout.")
