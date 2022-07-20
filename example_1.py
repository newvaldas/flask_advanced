from flask import Flask

app = Flask(__name__)

@app.route("/<name>") #enter user input after / and returns in "Hello, {name}"
def user(name):
 return f"Hello, {name}"

if __name__ == "__main__":
 app.run(debug=True)
 
 