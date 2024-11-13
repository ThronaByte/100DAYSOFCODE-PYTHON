from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


posts = requests.get("https://api.npoint.io/267632ac854a79713c11").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:number>")
def show_post(number):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == number:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

