from flask import Flask
from random import randint
random_num = randint(-1, 10)


def check_guess(function):
    def wrapper(*args, **kwargs):
        print(args)
        # if args[0] == random_num:
        #     return 'You found me! '
        # elif args[0] < random_num:
        #     return 'Too Low, try again! '
        # else:
        #     return 'Too high, try again! '

    return wrapper


app = Flask(__name__)


@app.route("/")
def home():
    return '<h1 > Guess the number</h1>'\
            '<img src="https://media.giphy.com/media/eCAoHEREmZtCtsaosu/giphy.gif" width=350>'


@app.route('/<int:usr_guess>')
@check_guess
def guess(usr_guess):
    pass









if __name__ == "__main__":
    app.run(debug=True)