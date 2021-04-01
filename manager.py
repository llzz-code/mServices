import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        pass


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler)
    ])


if __name__ == '__main__':
    app = None