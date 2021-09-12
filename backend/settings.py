# 注意生产环境需要禁用以下配置项
import os
DEBUG = True
TESTING = True
SQLALCHEMY_ECHO = True
###########################
SECRET_KEY = b'k\x87\xbaF\x93\x85N\x04m\xfc\xbe\xb6\x1a[\x16\xd1' \
    if DEBUG else os.urandom(16)
# 注意生产环境下未必是这个账号密码
# Y-jiji的电脑上账号密码都是root
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/brog_db'
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 2 * 60 * 60
SQLALCHEMY_MAX_OVERFLOW = 10
SQLALCHEMY_TRACK_MODIFICATIONS = True
ALLOWED_HOSTS = ['http://localhost:8080', ]  # 目前只是调试
