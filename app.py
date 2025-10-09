from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os
from flask import Flask, render_template


app = Flask(__name__)

app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///database.db"
)

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
