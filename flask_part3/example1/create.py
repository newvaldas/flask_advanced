from app import db, Message

db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
tomas = Message('Tomas', 'tomas@mail.com', 'Tomas sako, Sveiki!', 86123456)
romas = Message('Romas', 'romas@pastas.lt', 'Ar viskas cia veikia.', 888888888)
marius = Message('Marius', 'marko@friends.lt', 'As esu Marius', '123123123')
bronius = Message('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.', 123456789)
petras = Message('Petras', 'petro@pastas.lt', 'Petrui labai linksma.', 111111111)

# Pridėsime šiuos veikėjus į mūsų DB
db.session.add_all([tomas, romas, marius, bronius, petras])
# .commit išsaugo pakeitimus
db.session.commit()

print(tomas.id)
print(romas.id)
print(marius.id)
print(bronius.id)
print(petras.id)
