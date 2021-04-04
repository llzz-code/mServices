from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from utils.conn import Base

class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    content = Column(Text)
    category_id = Column(Integer)
    time = Column(DateTime)