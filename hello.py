import json

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
import tornado.options

class IndexHandler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        name = self.get_query_argument('name')
        city = self.get_query_argument('city')

        self.write('<h3>Hello, Tornado_get %s %s</h3>' % (name, city))


    def post(self):
        name = self.get_argument('name')
        city = self.get_argument('city')
        self.write('<h3>%s %s</h3>' % (name, city))


class SearchHandler(RequestHandler):
    mapper = {
        'python': 'nice呀',
        'Java': 'nice too呀'
    }

    def get(self):
        html = """
            <h3>搜索%s结果</h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)
        # self.write(html % (wd, result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))
        self.set_status(200)
        # self.set_header('Content-Type', 'application/json:charset=utf-8')

class CookieHandler(RequestHandler):
    def get(self):
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            value = self.get_cookie(name)
            print(type(value))
            self.write(value)
        else:
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key, value in cookies.items():
                lis.append('<li>%s: %s</li>' % (key, value))
            self.write('显示所有' + html % ''.join(lis))

    # def delete(self):
    #     name = self.get_argument('name')
    #     if self.request.cookies.get(name, None):
    #         self.clear_cookie(name)
    #         self.write('<h2>删除%s 成功</h2>' % name)
    #     else:
    #         self.write('<h2>无cookies</h2>')
    # self.redirect('cookie')  重定向

class OrderHandler(RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'Python3',
            'author': 'lz',
            'price': 100
        },
        {
            'id': 2,
            'name': 'Python2',
            'author': 'lz',
            'price': 150
        }
    ]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }
    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def initialize(self):
        # 所有请求方法再调用前，都会进行初始化
        print('------initialize----')

    def prepare(self):
        # 在预处理之后，在行为方法之前
        print('--------prepare-----')
        # 主要用于验证参数、权限、读取缓存

    def on_finish(self):
        # 在请求行为方法之后，释放资源
        print('---finish----')




    def get(self, order_id, action_code):
        html = """
            <p>
                商品编号: %s
            </p>
            <p>
                商品名称: %s
            </p>
            <p>
                商品价格: %s
            </p>
        """
        goods = self.query(int(order_id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(action_code)))




def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(\d+)/(\d+)', OrderHandler)
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port',
                           default=7000,
                           type=int,
                           help='bind socket port')

    tornado.options.define('host',
                           default='localhost',
                           type=str,
                           help='设置host name')

    # 解析命令行参数
    tornado.options.parse_command_line()
    # # 创建web应用
    # app = Application([
    #     ('/', IndexHandler)
    # ])
    # app.listen(7000)
    app = make_app()
    app.listen(tornado.options.options.port)

    # 启动web服务
    print('Starting http://%s:%s' % (
        tornado.options.options.host,
        tornado.options.options.port))
    IOLoop.current().start()


