from app import Publisher, Author, Book, db


books = Book.query.all()

print(books)

# for book in books:
#     print(f"{book.title}, {book.authors}")


# author1 = Author.query.filter_by(fname="Valdas").first()

# print(f"pirmo autoriaus knygos: {author1.books}")

# print(dir(author1))