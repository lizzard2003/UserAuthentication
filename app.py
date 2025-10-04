from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)  # Creates the database instance
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"\
app.config['SECRET_KEY']= 'thisisasecretkey'


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
    app.run(debug=True)
