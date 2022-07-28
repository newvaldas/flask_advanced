from flask import Flask

app = Flask(__name__) 

@app.route("/") # path'as po / 
def home():
 return "This is may new page.<h1></h1>"

if __name__ == "__main__": #
 app.run(debug=True) # run paleidzia app