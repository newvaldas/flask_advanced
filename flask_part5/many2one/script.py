from app import Vaikas, Tevas, db

# v1 = Vaikas("Vaikas", "Vaiksonas")

# t1 = Tevas("Tevas", "Patevis", 1)

# db.session.add_all([v1, t1])
# db.session.commit()

vaikai = Vaikas.query.all()
# print(vaikai)
print(dir(vaikai[0].tevai[0].pavarde))

tevai = Tevas.query.all()
# print("Tevas")
# print((tevai[0].vaikas.pavarde))