from flask import Flask, redirect, url_for, render_template, request, session

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "12345678"
app.permanent_session_lifetime = timedelta(minutes=5)  # other options include "days"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # making the session permanent that means it persists even after the webpage is closed
        username = request.form["nm"]
        session["username"] = username
        return redirect(url_for("user"))
    else:
        if "username" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
