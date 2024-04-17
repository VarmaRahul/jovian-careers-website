from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/test')
def hello():
    return 'Hello, this is test website'


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)