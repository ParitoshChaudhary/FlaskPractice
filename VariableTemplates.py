from flask import Flask, render_template

app = Flask(__name__)

@app.route("/name/<name>")
def indexName(name):
    letters = list(name)
    name_dict = {'name' : name}
    return render_template('variable.html', name = name, letters = letters,
                            name_dict = name_dict)

if __name__ == '__main__':
    app.run(debug=True)
