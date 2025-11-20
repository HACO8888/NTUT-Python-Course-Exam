class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added book: {book}')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Removed book: {book}')
        else:
            print(f'Book not found: {book}')

    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

    def list_books(self):
        return self.books 
      
library = Library()
library.add_book({'title': 'Book A', 'author': 'Author 1'})
library.add_book({'title': 'Book B', 'author': 'Author 2'})
print("All books:", library.list_books())
found_book = library.find_book('Book A')
print("Found book:", found_book)
library.remove_book({'title': 'Book A', 'author': 'Author 1'})
print("All books after removal:", library.list_books())