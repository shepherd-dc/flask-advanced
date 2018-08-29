class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = book['author']
        self.publisher = book['publisher']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        self.total = books.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in books.books]