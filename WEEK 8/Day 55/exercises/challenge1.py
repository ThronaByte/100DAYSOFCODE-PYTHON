from flask import Flask


app =  Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b> {function()} </b>'
    return wrapper


def emphasis(function):
    def wrapper():
        return f'<em> {function()}  </em>'
    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u> {function()} </u>'
    return  wrapper


def center(function):
    def wrapper():
        return f'<center> {function()} </center>'
    return wrapper


@app.route('/')
@make_bold
@emphasis
@make_underlined
@center
def test():
    return ("<h1 style='color: purple'>Remember, every coder was once a beginner."
            "Python might feel challenging now, but every small step forward is progress."
            "Keep going, and soon you’ll look back amazed at how far you’ve come. You've got this! 'B'</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnprNnU4YWxidWpxNWN5czVoYzNleTI1aDF1dGJ2bHpjeGliYWRoeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YVpIaYgJ3lpMk/giphy.gif'>")


if __name__ == '__main__':
    app.run(debug=True)