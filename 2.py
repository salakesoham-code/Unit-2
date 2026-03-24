class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True   # Book is available by default

    def check_out(self):
        if self.available:
            self.available = False
            print(f'"{self.book_name}" has been checked out.')
        else:
            print(f'Sorry, "{self.book_name}" is not available.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.book_name}" has been returned.')
        else:
            print(f'"{self.book_name}" was not checked out.')

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print(f'Book: {self.book_name}')
        print(f'Author: {self.author}')
        print(f'Status: {status}')
        print("-" * 30)


# Example Usage
book1 = Library("Python Programming", "John Smith")
book2 = Library("Data Structures", "Alice Brown")

book1.display_book()
book1.check_out()
book1.display_book()
book1.return_book()
book1.display_book()
