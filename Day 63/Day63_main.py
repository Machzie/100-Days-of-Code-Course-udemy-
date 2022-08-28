from flask import Flask, render_template, request, redirect, url_for
import sqlite3

with sqlite3.connect("book-collection.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books ("
               "id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE, "
               "author varchar(250) NOT NULL, "
               "rating FLOAT NOT NULL)")


app = Flask(__name__)


@app.route('/')
def home():
    with sqlite3.connect("book-collection.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from books")
        all_books = cursor.fetchall()
        return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    with sqlite3.connect("book-collection.db") as db:
        cursor = db.cursor()
        if request.method == "POST":
            title = request.form["title"]
            author = request.form["author"]
            rating = request.form["rating"]
            print(title, author, rating)
            cursor.execute("INSERT INTO books VALUES(NULL, ?, ?, ?)", (str(title), str(author), float(rating)))
            db.commit()
            return redirect(url_for("home"))
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

