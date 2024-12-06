class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author




library = Library('Costa Rica National Library')
book1 = Book('Jujutsu Kaisen...', 'Satoru Goyo')
book2 = Book('Boku no Hero....', 'None')
book3 = Book('Akebis Sailor Uniform', 'Anyone')


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print(library.name)
print(library.list_books())

print('----------------------')

for book in library.list_books():
    print(book)