from tornado.web import RequestHandler

from app.models.blogs import Blogs
from app.models.category import Category
from app.models.menu import Menu
from utils.conn import session


class BlogHandler(RequestHandler):

    navs = {}
    blog_navs = {}

    def initialize(self):
        # 左侧导航栏
        self.navs = session.query(Menu).filter(Menu.parent_id == '').all()

        # 管理员导航栏
        self.blog_navs = session.query(Menu).filter(Menu.parent_id == 2)

    def get(self):
        id = self.get_query_argument('id', '1')
        blog_list = session.query(Blogs.id, Blogs.title, Blogs.content, Blogs.time, Category.name)\
            .join(Category, Category.id == Blogs.id).all()
        blog_con = session.query(Blogs.id, Blogs.title, Blogs.content, Blogs.time, Category.name)\
            .join(Category, Category.id == Blogs.id)\
            .filter(Blogs.id == id).first()

        data = {
            'blog_navs': self.blog_navs,
            'blogs': blog_list,
            'navs': self.navs,
            'index': False,
            'blog_con': blog_con
        }

        self.render('blog_list.html', **data)
