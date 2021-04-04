from tornado.web import RequestHandler

from app.models.admin import Admin
from app.models.menu import Menu
from utils.conn import session


class IndexHandler(RequestHandler):
    navs = {}
    admin_navs = {}

    def initialize(self):
        # 左侧导航栏
        self.navs = session.query(Menu).filter(Menu.parent_id == '').all()
        # 管理员导航栏
        self.admin_navs = session.query(Menu).filter(Menu.parent_id == 1)

    def get(self):
        admin_list = session.query(Admin).filter(Admin.deleted != 1).all()
        deleted = session.query(Admin).filter(Admin.deleted == 1).all()
        data = {
            'admin_navs': self.admin_navs,
            'admins': admin_list,
            'deleted': deleted,
            'navs': self.navs,
            'index': False
        }

        self.render('admin_list.html', **data)

    def delete(self):
        id = self.get_argument('id')
        res = session.query(Admin).filter(Admin.id == id).first()
        res.purview = -1
        res.deleted = 1
        session.commit()
        session.close()

    def put(self):
        id = self.get_argument('id')
        res = session.query(Admin).filter(Admin.id == id).first()
        res.purview = 0
        res.deleted = 0
        session.commit()
        session.close()
    def on_finish(self):
        print('finish')
        session.close()
