from sqlalchemy import Column, ForeignKey, Integer, String, orm

from base import Base

class User(Base):
    """
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String)

    def __repr__(self):
        return 'User(name={0})'.format(self.name)
