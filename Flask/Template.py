from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# /means the default domain
# You can also use @app.route("/")


@app.route("/<name>")
def home(name):
    # render HTML code
    return render_template("index.html", content=name, r=2)


if __name__ == "__main__":
    app.run()
