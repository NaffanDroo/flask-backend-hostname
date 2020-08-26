from flask import Blueprint, url_for
from werkzeug.utils import redirect

root = Blueprint('root', __name__)


@root.route('/')
def index():
    return redirect(url_for('hostname.host'))
