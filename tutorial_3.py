from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("child.html")


@app.route("/new")
def new():
    return render_template("new.html")


if __name__ == "__main__":
    app.run(
        debug=True
    )  # auto detects changes and does updates, don't have to re-run the server on each updation in the code
