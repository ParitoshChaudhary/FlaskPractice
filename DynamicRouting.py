from flask import Flask
app = Flask(__name__)

@app.route("/name/<name>")
def name(name):
    return f"<h1> THIS IS A MESSAGE TO WELCOME {name}<h1>"

@app.route("/name_up/<name>")
def nameUpper(name):
    return f"<h1> THIS IS A MESSAGE FOR UPPER {name.upper()}<h1>"

@app.route("/name_number/<name>")
def nameLetter(name):
    return f"<h1> 2nd LETTER IN THE NAME {name} IS : {name[15]}"

if __name__ == "__main__":
    app.run(debug = True)
