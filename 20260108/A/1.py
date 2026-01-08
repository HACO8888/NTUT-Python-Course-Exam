class Book:
    def __init__(self, isbn, title, status_code):
        self.isbn = isbn
        self.title = title
        self.is_available = True if status_code == "1" else False

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"Successfully borrowed {self.title}."
        else:
            return "此書已借出"

    def return_book(self):
        self.is_available = True

    def format_for_save(self):
        status_code = "1" if self.is_available else "0"
        return f"{self.isbn},{self.title},{status_code}"


def load_books(filename):
    library = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            isbn, title, status_code = line.strip().split(",")
            library[isbn] = Book(isbn, title, status_code)
    return library


def process_actions(library, filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            action, isbn = line.strip().split(",")
            if isbn in library:
                book = library[isbn]
                if action == "BORROW":
                    print(book.borrow_book())
                elif action == "RETURN":
                    book.return_book()


def save_library_status(library, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for book in library.values():
            file.write(book.format_for_save() + "\n")


if __name__ == "__main__":
    library = load_books("books.txt")
    process_actions(library, "actions.txt")
    save_library_status(library, "library_status.txt")
