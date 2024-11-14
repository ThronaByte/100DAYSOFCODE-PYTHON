import os
from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv(".env")


PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIL')

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/ec6f9af19082e8780b3f").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data.get('name'), data.get('email'), data.get('phone'), data.get('message'))
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(
            user=EMAIL,
            password=PASSWORD
        )
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=email_message
        )

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
