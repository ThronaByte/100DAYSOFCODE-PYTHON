from flask import Flask

app = Flask(__name__)
@app.route('')


@app.route('/')
def home():
    return '<h1>Hello World</h1>'\
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDh3c2dmZWY2ZzN3MTBtZDZ4bjRibGl5MmIwMzVuNjlrbDkyZDYxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dmDFK7YkvdyNi/giphy.gif"</img>'


@app.route('/username/<name>/<int:number>')
def test(name, number):
    return f"Hello dear {name} your id is {number}!"


if __name__ == '__main__':
    app.run(debug=True)
