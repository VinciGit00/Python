from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# /means the default domain
# You can also use @app.route("/")


@app.route("/")
def home():
    # render HTML code
    return render_template("Base.html", content="Testing")


if __name__ == "__main__":
    app.run(debug=True)