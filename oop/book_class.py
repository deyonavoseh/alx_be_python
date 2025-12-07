class Book:
    """A class representing a book with title, author, and year."""
    
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a message when the book is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Return a user