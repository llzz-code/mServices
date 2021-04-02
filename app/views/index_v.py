from tornado.web import RequestHandler


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