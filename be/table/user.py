from sqlalchemy import Column, Integer, String, Text
from be.model.database import Base


class User(Base):
    __tablename__ = 'user'
    user_id = Column(String(240), primary_key=True)
    password = Column(String(240), nullable=True)


    def __init__(self, user_id=None, password=None):
        self.user_id = user_id
        self.password = password


    def __repr__(self):
        return '<User %r,%r>' % (self.user_id,self.password)
