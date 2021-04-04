from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from utils.conn import Base


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False)
    url = Column(String(50), nullable=True)
    # parent_id = Column(Integer, nullable=True)
    parent_id = Column(Integer, ForeignKey('menu.id', name='parent_id_fk'))
    children = relationship('Menu')
    # def __str__(self):
    #     return "%s %s" % (self.parent_id, self.children)




