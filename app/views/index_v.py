from tornado.web import RequestHandler

from app.models.menu import Menu
from utils.conn import session


class IndexHandler(RequestHandler):
    def initialize(self):
        pass


    def get(self):
        navs = session.query(Menu).filter(Menu.parent_id == '').all()

        data = {
            'msg': 'hi, Template',
            'error_msg': None,
            'navs': navs,
            'index': True
        }
        for nav in navs:
            print(nav.title)
        self.render('base.html', **data)

    def post(self):
        # 向客户端响应数据
        name = self.get_query_argument('name')
        city = self.get_query_argument('city')

        self.write('<h3>Hello, Tornado_get %s %s</h3>' % (name, city))

    def put(self):
        name = self.get_argument('name')
        city = self.get_argument('city')
        self.write('<h3>%s %s</h3>' % (name, city))
