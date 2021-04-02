import tornado.options as options
from tornado.ioloop import IOLoop

from app import make_app

if __name__ == '__main__':
    # 定义命令行参数
    options.define('port',
                   default=7000,
                   type=int,
                   help='bind socket port')

    options.define('host',
                   default='localhost',
                   type=str,
                   help='设置host name')

    # 解析命令行参数
    options.parse_command_line()
    # # 创建web应用
    # app = Application([
    #     ('/', IndexHandler)
    # ])
    # app.listen(7000)
    app = make_app(options.options.host)
    app.listen(options.options.port)

    # 启动web服务
    print('Starting http://%s:%s' % (
        options.options.host,
        options.options.port))
    IOLoop.current().start()
