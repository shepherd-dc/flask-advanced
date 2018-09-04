from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
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

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn)\
            .filter(Wish.launched==False,
                   Wish.isbn.in_(isbn_list),
                   Wish.status==1)\
            .group_by(Wish.isbn).all()
        count_list = [{"count": w[0], "isbn": w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        book = Book()
        book.search_by_isbn(self.isbn)
        return book.first