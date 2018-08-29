from flask import jsonify, request, json

from app.forms.book import SearchForm
from app.view_models.book import BookCollection
from . import web
from app.spider.book import Book
from app.libs.helper import is_isbn_or_key


@web.route('/book/search')
def search():
    '''
    /book/search?q=金庸&page=1
    '''
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        bookData = Book()
        if isbn_or_key == 'isbn':
            bookData.search_by_isbn(q)
        else:
            bookData.search_by_keyword(q, page)

        books.fill(bookData, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)