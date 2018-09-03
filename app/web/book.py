from flask import jsonify, request, json, render_template, flash
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import TradeInfo
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
    has_in_gifts = False
    has_in_wishes = False

    # 获取书籍详情数据
    book = Book()
    book.search_by_isbn(isbn)
    book_details = BookViewModel(book.first)
    # return jsonify(book_detail.__dict__)
    # return json.dumps(book_detail, default=lambda o: o.__dict__)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True


    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book_details, gifts=trade_gifts_model, wishes=trade_wishes_model,
                           has_in_gifts = has_in_gifts, has_in_wishes = has_in_wishes)
