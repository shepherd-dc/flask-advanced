from flask import jsonify, request, json, render_template, flash

from . import web

from app.view_models.book import BookCollection, BookViewModel
from app.spider.book import Book
from app.libs.helper import is_isbn_or_key
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
    /book/search?q=金庸&page=1
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        book_data = Book()
        if isbn_or_key == 'isbn':
            book_data.search_by_isbn(q)
        else:
            book_data.search_by_keyword(q, page)

        books.fill(book_data, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('搜索关键字有误，请重新输入')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    book = Book()
    book.search_by_isbn(isbn)
    book_detail = BookViewModel(book.first)
    # return jsonify(book_detail.__dict__)
    # return json.dumps(book_detail, default=lambda o: o.__dict__)
    return render_template('book_detail.html', book=book_detail, wishes=[], gifts=[])
