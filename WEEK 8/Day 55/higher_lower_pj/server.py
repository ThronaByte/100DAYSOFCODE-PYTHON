from flask import Flask
import random

HIGH = '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3o4MnIyY2Jrcm4xZW95ZTk3ZjJ3MHFidXlzY2o4czM5bGRxOWdhYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/U4jM3IeIVd6VOyeLa7/giphy.gif">'
LOW = '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW5nZmVrOG51M2E1bG56NDRhNzNrM29zMXBoemRhbmpja3cxejg3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif">'
CORRECT = '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTl1a3VpbGttaTVybXRhMDVxamNycnJuY3pwOTRqM2ZiZHZvODJubCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.gif">'

goal = random.randint(0,9)
print(goal)

app = Flask(__name__)


@app.route('/')
def home():
    return ('<h1 style="color: green">Guess a number between 0 and 9</h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmF0bjNteWI4cmxpOWFkcHVxYm16NWE3MWU5d25haXN6bWtibTY5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ne3xrYlWtQFtC/giphy.gif">')


@app.route('/<int:number>')
def correct_number(number):
    if  number > goal:
        return (f'<h1 style="color: purple">Too high, try again!</h1>'
                f'{HIGH}')

    elif number < goal:
        return (f'<h1 style="color: red">Too low, try again!</h1>'
                f'{LOW}')

    else:
        return (f'<h1 style="color: green">You found me!</h1>'
                f'{CORRECT}')


if __name__ == '__main__':
    app.run(debug=True)