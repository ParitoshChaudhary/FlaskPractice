from flask import Flask
app = Flask(__name__)

@app.route("/")
def homePage():
    return "<h1> THIS IS THE HOME PAGE !! <h1>"

@app.route("/puppy_latin/<name>")
def latinPuppy(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'itful'
    else:
        pupname = name + 'y'

    return f"<h1> YOUR PUPLATIN NAME IS {pupname}"

if __name__ == '__main__':
    app.run(debug=True)
