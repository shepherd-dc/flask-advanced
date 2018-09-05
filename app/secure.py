import os
from datetime import timedelta

DEBUG = True
SECRET_KEY = os.urandom(24)
REMEMBER_COOKIE_DURATION = timedelta(days=7)
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'cymysql'
USERNAME = 'root'
PASSWORD = 123456
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'fisher'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '347928429@qq.com'
MAIL_PASSWORD = 'bsqsoafeebyzcach'