from flask import render_template, flash

from . import web


@web.route('/test')
def test():
    flash('flash test1', category='error')
    flash('flash test2', category='warning')
    return render_template('test.html')