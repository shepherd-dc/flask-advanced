from contextlib import contextmanager
from datetime import datetime

from flask import flash
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Integer, SmallInteger, Column


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, msg='操作成功'):
        try:
            yield
            self.session.commit()
            flash(msg)
        except Exception as e:
            self.session.rollback()
            raise e


class MyQuery(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(MyQuery, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=MyQuery)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0
