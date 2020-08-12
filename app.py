import socket
import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

payload = {'backend_host': socket.gethostname()}


@app.route('/', methods=['GET'])
def home():
    return jsonify(payload)
