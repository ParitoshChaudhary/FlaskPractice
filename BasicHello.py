from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> THIS IS THE FIRST PAGE FROM FLASK<h1>'

if __name__ == '__main__':
    app.run()
