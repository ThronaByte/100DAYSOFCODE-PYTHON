from flask import render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os
from dotenv import load_dotenv


load_dotenv(".env")
app = Flask(__name__)


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# #"sqlite:///books-collection.db"

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250),nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    query = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = query.scalars().all()
    return render_template(template_name_or_list='index.html', books=all_books)


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if query:
        results = Book.query.filter(
            Book.title.ilike(f"%{query}%") |
            Book.author.ilike(f"%{query}%")
        ).all()
    else:
        results = []
    return render_template("search.html", books=results)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )

        db.session.add(new_book)
        db.session.commit()
        # print("Result added t0 db")
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        new_rating = request.form["rating"]

        # Validate the rating
        try:
            new_rating = float(new_rating)
            if new_rating < 0 or new_rating > 10:
                error_message = "Rating must be between 0 and 10."
                book_to_update = Book.query.get_or_404(book_id)
                return render_template('edit_rating.html', book=book_to_update, error=error_message)
        except ValueError:
            error_message = "Please enter a valid number for the rating."
            book_to_update = Book.query.get_or_404(book_id)
            return render_template('edit_rating.html', book=book_to_update, error=error_message)

        # Update the rating if validation passes
        book_to_update = Book.query.get_or_404(book_id)
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    # GET request
    book_id = request.args.get("id")
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit_rating.html', book=book_selected)

@app.route(rule='/delete')
def delete():
    book_id = request.args.get("id")
    book_to_delete = Book.query.get_or_404(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

