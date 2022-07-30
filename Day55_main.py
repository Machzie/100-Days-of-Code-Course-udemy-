# Day 55 Project - Higher Lower Web Game
from flask import Flask
import random

app = Flask(__name__)

number = random.randrange(0, 9, 1)


@app.route('/')
def welcome():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<iframe src="https://giphy.com/embed/ne3xrYlWtQFtC" width="480" height="205" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route('/<int:guess>')
def function1(guess):
    if guess > number:
        return f'<h1 style="color:purple">Too high!</h1>' \
               f'<iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="480" height="453" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    elif guess < number:
        return f'<h1 style="color:red">Too low!</h1>' \
               f'<iframe src="https://giphy.com/embed/jD4DwBtqPXRXa" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    else:
        return f'<h1 style="color:green">Correct!</h1>' \
               f'<iframe src="https://giphy.com/embed/4T7e4DmcrP9du" width="458" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


if __name__ == "__main__":
    app.run()
