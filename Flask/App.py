from flask import Flask, redirect, url_for

app = Flask(__name__)

# /means the default domain
# You can also use @app.route("/")


@app.route("/")
def home():
    # You can even add HTML code
    return "<h1>Hello world</h1>"


@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}!</h1>"


@app.route("/admin")
def admin():
    # Redirect to a different page
    # Redirect to home
    return redirect(url_for("home"))

# Instead if I need a parameter to run:


@app.route("/admin2")
def admin2():
    return redirect(url_for("user", name="Peppino"))

# Double route


@app.route("/a/b")
def doubleRoute():
    return "<h1>Double route/h1>"


if __name__ == "__main__":
    app.run()
