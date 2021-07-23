from ext import db
from sqlalchemy import Column, Integer, String
import random as rand
import string


class User(db.Model):
    def __init__(self, name, pwd, ip) -> None:
        super().__init__()
        self.name = name
        self.pwd = pwd
        self.ip = ip
    id = Column(Integer, primary_key=True, autoincrement=True)  # 创建id列，并设置为主键
    name = Column(String(80), unique=True)  # 创建username列，设置为不可重复
    pwd = Column(String(80))
    token = Column(
        String(50),
        default=lambda: ''.join(rand.choices(string.ascii_letters + string.digits, k=50)),
        onupdate=lambda: ''.join(rand.choices(string.ascii_letters + string.digits, k=50))
    )
    ip = Column(String(40), default=None)
