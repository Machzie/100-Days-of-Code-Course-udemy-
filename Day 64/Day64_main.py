from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import requests
import Day64_config as config

with sqlite3.connect("films.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS films ("
                   "id INTEGER PRIMARY KEY,"
                   "title VARCHAR(250) NOT NULL,"
                   "year INTEGER,"
                   "description VARCHAR(250),"
                   "rating FLOAT,"
                   "review VARCHAR(250),"
                   "img_url VARCHAR(250))")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def home():
    with sqlite3.connect("films.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM films "
                       "ORDER BY rating DESC "
                       "LIMIT 10")
        all_films = cursor.fetchall()
        return render_template("index.html", films=all_films)


class EditMovieForm(FlaskForm):
    rating = StringField("Your rating (/10)", validators=[DataRequired()])
    review = TextAreaField("Your review", validators=[DataRequired()])
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")


@app.route("/edit/<film_id>", methods=["GET", "POST"])
def update_film(film_id):
    update_form = EditMovieForm()
    if update_form.validate_on_submit():
        if update_form.submit.data:
            new_rating = update_form.rating.data
            new_review = update_form.review.data
            with sqlite3.connect("films.db") as db:
                cursor = db.cursor()
                cursor.execute("UPDATE films "
                               "SET rating = ?, review = ? "
                               "WHERE id = ?",
                               (new_rating, new_review, film_id))
                db.commit()
        elif update_form.cancel.data:
            pass
        return redirect(url_for('home'))
    return render_template("edit.html", form=update_form)


@app.route("/delete/<film_id>")
def delete_film(film_id):
    with sqlite3.connect("films.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE from films "
                       "WHERE id = ?",
                       (film_id,))
        db.commit()
    return redirect(url_for('home'))


class AddMovieForm(FlaskForm):
    name = StringField("Film title:", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/add", methods=["GET", "POST"])
def add_film():
    add_form = AddMovieForm()
    film_title = add_form.name.data
    if add_form.validate_on_submit():
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                params={"api_key": config.API_key, "query": film_title})
        film_data = response.json()["results"]
        return render_template("select.html", film_options=film_data)
    return render_template("add.html", form=add_form)


@app.route("/find/<TMDB_id>")
def find_film(TMDB_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{TMDB_id}",
                            params={"api_key": config.API_key})
    detailed_film_data = response.json()
    film_title = detailed_film_data["title"]
    film_year = detailed_film_data["release_date"][:4]
    film_img_url = f"https://www.themoviedb.org/t/p/w1280{detailed_film_data['poster_path']}"
    film_description = detailed_film_data["overview"]

    with sqlite3.connect("films.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO films "
                       "VALUES(NULL, ?, ?, ?, NULL, NULL, ?)",
                       (film_title, film_year, film_description, film_img_url))
        db.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
