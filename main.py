from flask import Flask

from blueprints.hostname import hostname
from blueprints.root import root


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.register_blueprint(hostname)
    app.register_blueprint(root)
    return app


app = create_app()