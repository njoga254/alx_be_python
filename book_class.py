# book_class.py

class Book:
    def __init__(self, title, author, year):
        "Constructor"
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor to clean up when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for informal display."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Book class
    book1 = Book("1984", "George Orwell", 1949)
    
    # Informal string representation
    print(str(book1))  # Output: 1984 by George Orwell, published in 1949
    
    # Official string representation
    print(repr(book1))  # Output: Book('1984', 'George Orwell', 1949)
    
    # Deleting the book1 object
    del book1