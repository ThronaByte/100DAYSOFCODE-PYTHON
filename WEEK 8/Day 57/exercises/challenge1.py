from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

# year = datetime.today().year
# print(year)
@app.route('/')
def home():
    year = datetime.today().year
    return  render_template('index.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)