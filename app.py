from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/greet/')
def greet():
    return "Hello and Good morning User!"


if __name__ == '__main__':
    app.run(debug=True)
