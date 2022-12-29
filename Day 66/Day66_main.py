from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Retrieve Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe))
    all_cafes_list = cafes.scalars().all()
    random_cafe = random.choice(all_cafes_list)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe))
    all_cafes_list = cafes.scalars().all()
    return jsonify(cafe=[cafe_i.to_dict() for cafe_i in all_cafes_list])


@app.route("/search", methods=["GET"])
def get_searched_cafes():
    query_location = request.args.get("loc").capitalize()
    cafes = db.session.execute(db.select(Cafe).filter_by(location=query_location))
    filtered_cafes_list = cafes.scalars().all()
    if filtered_cafes_list:
        return jsonify(cafe=[cafe_i.to_dict() for cafe_i in filtered_cafes_list])
    else:
        return f"Not found: Sorry, we don't have a cafe at location {query_location}", 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(int(request.form.get("sockets"))),
        has_toilet=bool(int(request.form.get("toilet"))),
        has_wifi=bool(int(request.form.get("wifi"))),
        can_take_calls=bool(int(request.form.get("calls"))),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return f"Success: {new_cafe.name} was successfully added", 200


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafes = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).first()
    if cafes:
        cafe_to_edit = cafes[0]
        cafe_to_edit.coffee_price = new_price
        db.session.commit()
        return f"Successfully updated the price of coffee at {cafe_to_edit.name} to {new_price}", 200
    else:
        return f"Not Found: There was no cafe with ID #{cafe_id} in the database", 404


# HTTP DELETE - Delete Record
@app.route("/report_closed/<int:cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafes = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).first()
        if cafes:
            cafe_to_delete = cafes[0]
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return f"Success: {cafe_to_delete.name} was successfully removed from the database", 200
        else:
            return f"Not Found: There was no cafe with ID #{cafe_id} in the database", 404
    else:
        return "Forbidden: Incorrect API Key", 403


if __name__ == '__main__':
    app.run(debug=True)
