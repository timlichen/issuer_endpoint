import os
from flask import Flask, request, render_template, jsonify, url_for, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/issuer.json')
def issuer():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "templates/", "issuer.json")
    data = json.load(open(json_url))
    return jsonify(data)

@app.route("/revocation.json")
def revocation():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "templates/", "revocation.json")
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)