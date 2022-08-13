from crypt import methods
from flask import Flask, request, jsonify

app = Flask(__name__)

# http: // 127.0.0.1: 5000/api?Query = ciao


@app.route("/api", methods=['GET'])
def hello_world():
    Query = str(request.args['Query'])
    return Query

# http://127.0.0.1:5000/json?Query=ciao
# http://127.0.0.1:5000/json?Query={nome: marco, cognome: vinciguerra, age:22}


@app.route("/json", methods=['GET'])
def json():
    # Creation of the vocaboulary
    d = {}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)


@app.route("/home", methods=['GET'])
def main():
    return "<h1>Hello world </h1>"


if __name__ == "__main__":
    app.run(debug=True)
