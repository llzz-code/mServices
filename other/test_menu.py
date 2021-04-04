from unittest import TestCase

from utils.conn import session, Base
from app.models.menu import Menu


class TeatMenu(TestCase):
    def test_creat(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

    def test_add(self):
        m1 = Menu()
        m1.title = '艹'
        m1.name = ''
        session.add(m1)
        if session.commit():
            print('success')

    def test_adds(self):
        session.add_all([
            Menu(title='orderManage'),
            Menu(title='vipManage', url='/user1', parent_id=1),
            Menu(title='friend', url='/user2', parent_id=1)
        ])
        session.commit()


    def test_get(self):
        m = session.query(Menu).get(1)
        print(m.title)
        print(m.children)

    def test_query_root_menu(self):
        ms = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for m in ms:
            print(m.title)




