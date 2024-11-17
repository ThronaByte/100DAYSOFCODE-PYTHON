from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app=app)

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# #MovieDb
class MovieDb(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=MovieDb)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

## RateMovieForm
class RateMovieForm(FlaskForm):
    rating = FloatField(
        label="Your Rating Out of 10 e.g. 7.5",
        validators=[DataRequired(), NumberRange(min=0, max=10, message="Rating must be between 0 and 10.")],
    )
    review = StringField(label="Your Review")
    done = SubmitField(label="Done")

# # Movie TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    paginated_movies = db.session.query(Movie).order_by(Movie.rating.desc(), Movie.title.asc()).paginate(page=page, per_page=per_page)

    # Adjust rankings based on current pagination.
    total_movies = paginated_movies.total
    for i, movie in enumerate(paginated_movies.items, start=(page - 1) * per_page + 1):
        movie.ranking = total_movies - i + 1
    db.session.commit()

    return render_template(template_name_or_list="index.html", movies=paginated_movies)


@app.route(rule='/edit', methods=["GET", "POST"])
def edit_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template(template_name_or_list='edit.html', movie=movie, form=form)


@app.route(rule='/delete')
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route(rule='/add', methods=["GET", "POST"])
def add():
    form = AddMovie()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url=TMDB_SEARCH_URL,  params={"api_key": TMDB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template(template_name_or_list="select.html", options=data)

    return render_template(template_name_or_list='add.html', form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{TMDB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": TMDB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{TMDB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for(endpoint="edit_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
