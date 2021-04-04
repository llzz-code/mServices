from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from utils.conn import Base


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    login_id = Column(String(18), nullable=False)
    password = Column(String(50), nullable=False)
    purview = Column(Integer, nullable=False)
    deleted = Column(Integer, nullable=True)


