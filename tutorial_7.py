from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = "12345678"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db.init_app(app)


# creating a model for our database (schema)


class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("child.html")


# viewing all the entries of the database
@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["nm"]
        session["username"] = username

        found_user = User.query.filter_by(name=username).first()

        if found_user:
            session["email"] = found_user.email
        else:
            usr = User(username, None)
            db.session.add(usr)
            db.session.commit()

        flash(f"login successful, {username}!!!")
        return redirect(url_for("user"))
    else:
        if "username" in session:
            username = session["username"]
            flash(f"already logged in, {username}")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "username" in session:
        username = session["username"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            found_user = User.query.filter_by(name=username).first()

            found_user.email = email
            db.session.commit()

            flash(f"email: {email} for user: {username} saved successfully!!!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("you are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "username" in session:
        username = session["username"]
        session.pop("username", None)
        session.pop("email", None)
        flash(f"Logged out successfully, {username}!!!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
