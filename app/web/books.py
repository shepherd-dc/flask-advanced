from flask import jsonify, request

from app.forms.book import SearchForm
from . import web
from book import Book
from helper import is_isbn_or_key


@web.route('/book/search')
def search():
    '''
    /book/search?q=金庸&page=1
    '''
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = Book.search_by_isbn(q)
        else:
            result = Book.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)