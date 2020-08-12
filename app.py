import socket
import flask
from flask import jsonify, redirect, url_for

app = flask.Flask(__name__)
app.config["DEBUG"] = True

payload = {'backend_host': socket.gethostname()}


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/v1/host', methods=['GET'])
def home():
    return jsonify(payload)
