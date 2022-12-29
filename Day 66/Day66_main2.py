from flask import Flask, jsonify, render_template, request
import sqlite3
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

## Cafe TABLE Configuration
# with sqlite3.connect("cafe_collection.db") as db:
#     cursor = db.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS Cafe ("
#                    "id INTEGER PRIMARY KEY,"
#                    "name varchar(250) NOT NULL UNIQUE,"
#                    "map_url varchar(250) NOT NULL,"
#                    "img_url varchar(250) NOT NULL,"
#                    "location varchar(250) NOT NULL,"
#                    "seats varchar(250) NOT NULL,"
#                    "has_toilet INTEGER NOT NULL,"
#                    "has_wifi INTEGER NOT NULL,"
#                    "has_sockets INTEGER NOT NULL,"
#                    "can_take_calls INTEGER NOT NULL,"
#                    "coffee_price varchar(250) NOT NULL)")


def to_DICT(cafe_choice):
    cafe_dict = {
        "id": cafe_choice[0],
        "name": cafe_choice[1],
        "location": cafe_choice[4],
        "seats": cafe_choice[5],
        "amenities": {
            "has_toilet": bool(cafe_choice[6]),
            "has_wifi": bool(cafe_choice[7]),
            "has_sockets": bool(cafe_choice[8])
        },
        "coffee_price": cafe_choice[10]
    }
    return cafe_dict


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Retrieve Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    with sqlite3.connect("cafe_collection.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from Cafe")
        all_cafes_list = cursor.fetchall()
        random_cafe = random.choice(all_cafes_list)
        return jsonify(cafe=to_DICT(random_cafe))


@app.route("/all", methods=["GET"])
def get_all_cafes():
    with sqlite3.connect("cafe_collection.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from Cafe")
        all_cafes_list = cursor.fetchall()
        return jsonify(cafe=[to_DICT(cafe_i) for cafe_i in all_cafes_list])


@app.route("/search", methods=["GET"])
def get_searched_cafes():
    query_location = request.args.get("loc").capitalize()
    with sqlite3.connect("cafe_collection.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from Cafe "
                       "WHERE location = ?",
                       (query_location,))
        filtered_cafes_list = cursor.fetchall()
        if filtered_cafes_list:
            return jsonify(cafe=[to_DICT(cafe_i) for cafe_i in filtered_cafes_list])
        else:
            return f"Not found: Sorry, we don't have a cafe at location {query_location}"


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    with sqlite3.connect("cafe_collection.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO Cafe (name, map_url, img_url, location, seats, has_toilet, has_wifi, "
                       "has_sockets, can_take_calls, coffee_price)"
                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (request.form.get("name"), request.form.get("map_url"),
                        request.form.get("img_url"), request.form.get("location"),
                        request.form.get("seats"), bool(int(request.form.get("toilet"))),
                        bool(int(request.form.get("wifi"))), bool(int(request.form.get("sockets"))),
                        bool(int(request.form.get("calls"))), request.form.get("coffee_price")))
        return f"Success: {request.form.get('name')} was successfully added"


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    with sqlite3.connect("cafe_collection.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from Cafe "
                       "WHERE id = ?",
                       (cafe_id,))
        cafe_to_edit = cursor.fetchone()
        if cafe_to_edit:
            cursor.execute("UPDATE Cafe "
                           "SET coffee_price = ? "
                           "WHERE id = ?",
                           (new_price, cafe_id))
            return f"Successfully updated the price of coffee at {cafe_to_edit[1]} to {new_price}", 200
        else:
            return f"Not Found: There was no cafe with ID #{cafe_id} in the database", 404


# HTTP DELETE - Delete Record
@app.route("/report_closed/<int:cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        with sqlite3.connect("cafe_collection.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * from Cafe "
                           "WHERE id = ?",
                           (cafe_id,))
            cafe_to_delete = cursor.fetchone()
            if cafe_to_delete:
                cursor.execute("DELETE from Cafe "
                               "WHERE id = ?",
                               (cafe_id,))
                return f"Success: {cafe_to_delete[1]} was successfully removed from the database", 200
            else:
                return f"Not Found: There was no cafe with ID #{cafe_id} in the database", 404
    else:
        return "Forbidden: Incorrect API Key", 403


if __name__ == '__main__':
    app.run(debug=True)
