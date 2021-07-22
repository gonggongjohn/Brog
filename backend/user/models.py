from ext import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id = Column(Integer, primary_key=True) # 创建id列，并设置为主键
    name = Column(String(80), unique=True) # 创建username列，设置为不可重复
    pwd = Column(String(80))

    def __init__(self, name, pwd): # 插入新值的方法
        super(User, self).__init__()
        self.name = name
        self.pwd = pwd

    def __repr__(self): # 输出的格式
        return '<User %r>' % self.name