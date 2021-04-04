from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from utils.conn import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))