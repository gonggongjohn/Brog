from ext import db
from sqlalchemy import *


class SearchWord(db.Model):
    __tablename__ = "Searchword"
    id = Column(type_=String(80),
                unique=True,
                primary_key=True)
    spelling = Column(String(50))
    fromFile = Column(String(50), ForeignKey(
        'file.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    major = Column(Integer)
