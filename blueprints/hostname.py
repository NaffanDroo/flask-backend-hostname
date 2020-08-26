import socket

from flask import Blueprint, jsonify

hostname = Blueprint('hostname', __name__, url_prefix='/v1')


@hostname.route('/host', methods=['GET'])
def host():
    return jsonify({'backend_host': socket.gethostname()})