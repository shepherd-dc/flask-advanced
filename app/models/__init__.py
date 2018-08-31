from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, SmallInteger, Column

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
