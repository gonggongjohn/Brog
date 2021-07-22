from ext import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True) # 创建id列，并设置为主键
    name = Column(String(80), unique=True) # 创建username列，设置为不可重复
    pwd = Column(String(80))