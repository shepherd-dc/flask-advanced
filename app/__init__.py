from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.user import User
from app.models.base import db
from app.web import web

login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    app.register_blueprint(web)


@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))
