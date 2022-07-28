
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    names = ['Jonas', 'Antanas', 'Petras']
    return render_template("names.html", names_list=names) 

if __name__ == "__main__":
    app.run(debug=True)