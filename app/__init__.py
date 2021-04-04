import os

from tornado.web import Application

from app.ui.nav import NavModule
from app.views.cookie_v import CookieHandler
from app.views.download import DownloadHandler
from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler
from app.views.admin.admin_index import IndexHandler as AdminHandler


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    ))

settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules': {
        'Nav': NavModule
    }
}


def make_app(host='localhost'):
    return Application(handlers=[
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(\d+)/(\d+)', OrderHandler),
        ('/admin/index', AdminHandler),
        ('/download', DownloadHandler)
    ], default_host=host,
        **settings)
