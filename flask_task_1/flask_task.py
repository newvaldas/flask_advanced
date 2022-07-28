# Užduotys

# 1. Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu (rekomenduojama naudoti šablonus)
# 2. Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio) ir paspaudus ENTER, atspausdintų jį penkis kartus.
# 3. Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.
# 4. Sukurti programą, kuri leistų įvesti metus ir paspaudus patvirtinimo mygtuką parodytų, ar jie yra keliamieji.

#==========Task1==========

# from flask import Flask

# task1 = Flask(__name__)

# @task1.route("/")
# def main():
#     return "<h1>This website for flask task!</h1>"

# if __name__ == "__main__":
#     task1.run(debug=True)

#==========Task2==========

from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def user(name):
 return f"Labas, {name}"

if __name__ == "__main__":
 app.run()