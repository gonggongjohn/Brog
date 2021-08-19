from ext import db
from sqlalchemy import *


class File(db.Model):
    __tablename__ = 'file'
    id = Column(type_=String(50),
                unique=True,
                primary_key=True)
    contributer = Column(String(50),ForeignKey('user.id', onupdate='CASCADE', ondelete='SET NULL'),nullable=True)
    filename = Column(String(100))

class Collection(db.Model):
    __tablename__ = 'collection'
    id = Column(type_=String(80),
                unique=True,
                primary_key=True)
    user_id = Column(String(50),ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'),nullable=True)
    file_id = Column(String(50),ForeignKey('file.id', onupdate='CASCADE', ondelete='CASCADE'),nullable=True)