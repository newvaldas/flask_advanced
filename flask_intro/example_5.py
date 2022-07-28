from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name_from_form = request.form['name']
        return render_template("greetings.html", name=name_from_form)
    else:
        return render_template("login.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)