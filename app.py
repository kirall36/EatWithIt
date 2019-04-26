from flask import Flask
from mymodels import *
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1> Eat With It App </h1>'


if __name__ == '__main__':
    app.run(debug=True)
