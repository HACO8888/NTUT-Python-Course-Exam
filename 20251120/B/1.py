class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"
      
book1 = Book("書本1", "作者A")
print(book1.get_info())