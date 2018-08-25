from flask import Flask, json

from book import Book
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
    return "<h1>Hello world~<h1>"


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    headers = {
        'content-type': 'application/json'
    }
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    return json.dumps(result), 200, headers


if __name__ == '__main__':
    app.run(host='0.0.0.0')
