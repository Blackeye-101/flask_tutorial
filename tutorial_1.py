from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>HOMEPAGE<h1>"


@app.route("/<name>")
def user(name):
    return f"hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Administrator"))


if __name__ == "__main__":
    app.run()
