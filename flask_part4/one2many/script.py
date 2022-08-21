from app import Publisher,db,  Book

publishers = Publisher.query.all()

try:
    print(publishers[0].books)
except:
    print("Cannot access publishers atribute books")

books = Book.query.all()
try:
    print(books[0].publisher)
except:
    print("Cannot access books atribute publisher")