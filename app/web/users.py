from . import web


@web.route('/user/login')
def login():
    return 'login'