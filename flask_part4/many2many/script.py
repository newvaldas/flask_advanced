from app import Publisher, Author, Book, db



pub1 = Publisher("Baltos Lankos")
pub2 = Publisher("Alma Littera")

book1 = Book("Bendra knyga", 1)
book2 = Book("Solo knyga", 1)
book3 = Book("Laba diena knyga", 2)
book4 = Book("Uztenka tu knygu", 2)

author1 = Author("Valdas", "Adamkus")
author2 = Author("Algimantas", "Cekuolis")
author3 = Author("Andrius", "Mamontovas")

book1.authors.append(author1)
book1.authors.append(author2)

book2.authors.append(author1)
book3.authors.append(author3)
book4.authors.append(author2)

db.session.add_all([pub1, pub2, book1, book2, book3, book4, author1, author2, author3])
db.session.commit()