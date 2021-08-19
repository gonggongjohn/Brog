from ext import db
from sqlalchemy import Column, String
import random as rand
import string


class User(db.Model):
    __tablename__ = 'user'
    id = Column(String(50), primary_key=True, unique=True)  # 创建id列，并设置为主键
    name = Column(String(80), unique=True)  # 创建username列，设置为不可重复
    pwd = Column(String(80))
    token = Column(
        String(50),
        default=lambda: ''.join(rand.choices(string.ascii_letters + string.digits, k=50)),
        onupdate=lambda: ''.join(rand.choices(string.ascii_letters + string.digits, k=50))
    )
    ip = Column(String(40), default=None)
