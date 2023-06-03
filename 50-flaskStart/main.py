from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f'<strong>{function.__name__}</strong>'

    return bold


def make_italic(function):
    def italic():
        return f'<em> {function.__name__} </em>'

    return italic


def make_underline(function):
    def underline():
        return f'<u> {function.__name__} </u>'

    return underline


# print(__name__)

@app.route('/')
@make_bold
# @make_underline
def hello_world():
    return 'Hello, World!'


@app.route('/<name>/<int:age>')
def greet(name, age):
    return f"Hello there {name}, you are {age} years old"


if __name__ == "__main__":
    app.run(debug=True)
