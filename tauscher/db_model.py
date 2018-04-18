from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{}')>".format(self.name)


class DB(object):
    def __init__(self, *args, **kwargs):
        self.base = declarative_base()
        self.engine = create_engine('sqlite:///tauscher.db')


    def create_all(self):
        self.base.metadata.create_all(self.engine)

if __name__ == '__main__':
    db = DB()
    db.create_all()
