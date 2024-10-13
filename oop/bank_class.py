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