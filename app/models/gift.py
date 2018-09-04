from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.spider.book import Book


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)

    @classmethod
    def recent(cls):
        recent_gifts = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOKS_COUNT']).distinct().all()
        return recent_gifts

    @property
    def book(self):
        book = Book()
        book.search_by_isbn(self.isbn)
        return book.first