from ext import db
from sqlalchemy import *


class File(db.Model):
    __tablename__ = 'file'
    id = Column(type_=Integer,
                primary_key=True, 
                autoincrement=True)
    
    contributer = Column(Integer,ForeignKey('user.id', onupdate='CASCADE', ondelete='SET NULL'),nullable=True)
