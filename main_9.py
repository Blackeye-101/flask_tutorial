from flask import Flask, render_template
from admin.tutorial_9 import tutorial_9

app = Flask(__name__)
app.register_blueprint(tutorial_9, url_prefix="/admin")


# blueprint route overrides the main file (common way to fix is to setup a url prefix)
@app.route("/")
def test():
    return "<h1>Test</h1>"


if __name__ == "__main__":
    app.run(debug=True)
