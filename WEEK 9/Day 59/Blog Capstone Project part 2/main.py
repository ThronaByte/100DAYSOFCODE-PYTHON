from flask import Flask, render_template
import requests
from datetime import datetime


n_point_api = requests.get("https://api.npoint.io/ec6f9af19082e8780b3f").json()

app = Flask(__name__)

def get_current_year():
    return datetime.today().year


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", all_posts=n_point_api, year=get_current_year())


@app.route("/about")
def about():
    return render_template("about.html", year=get_current_year())


@app.route("/contact")
def contact():
    return render_template("contact.html", year=get_current_year())


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in n_point_api:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=get_current_year())


if __name__ == "__main__":
    app.run(debug=True, port=5001)
