from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/blog?charset=utf8')


# 生成数据库连接的类
DbSession = sessionmaker(bind=engine)

# 创建会话类对象
session = DbSession()

# 生成所有模型类的父类
Base = declarative_base(bind=engine)

