from ext import db
from sqlalchemy import *


class File(db.Model):
    __tablename__ = 'file'
    id = Column(type_=String(50),
                unique=True,
                primary_key=True)
    contributer = Column(String(50),ForeignKey('user.id', onupdate='CASCADE', ondelete='SET NULL'),nullable=True)
    filename = Column(String(100))