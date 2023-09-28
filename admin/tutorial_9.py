from flask import Blueprint, render_template


tutorial_9 = Blueprint(
    "tutorial_9", __name__, static_folder="static", template_folder="templates"
)


@tutorial_9.route("/home")
@tutorial_9.route("/")
def home():
    return render_template("home.html")
