from flask import Flask
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000/
def index():
    return '<h1> THIS IS THE FIRST PAGE FROM FLASK<h1>'

@app.route('/info') #127.0.0.1:5000/info
def info():
    return "<h1> THIS IS THE SAMPLE INFORMATION<h1>"

if __name__ == '__main__':
    app.run()
