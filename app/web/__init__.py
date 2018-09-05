from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

from app.web import book, auth, drift, gift, main, wish
from app.web import test

