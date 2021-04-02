import json
import uuid

from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line


class LoginHandler(RequestHandler):
    users = [
        {
            'id': 1,
            'name': 'lz',
            'pwd': '123456',
            'last_login_device': 'Android 5.1 OnePlus5'
        }
    ]



    def get(self):
        pass

    
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type,x-requested-with')
        self.set_header('Access-Control-Allow-Methods',
                        'GET,POST,PUT,DELETE')



    def post(self):
        # 读取json数据
        byte = self.request.body
        print(byte)
        print(self.request.headers.get('Content-Type'))

        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            # self.write('upload json ok')
            json_str = byte.decode('utf-8')
            # 反序列化
            json_data = json.loads(json_str)
            login_user = None
            resp_data = {}
            for user in self.users:
                if user['name'] == json_data['name']:
                    if user['pwd'] == json_data['pwd']:
                        login_user = user
                        break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '用户不存在'

            self.write(resp_data)
            self.set_header('Content-Type', 'application/json')


        else:
            self.write('upload data 必须是Json格式')

        self.write('login---get')

    def put(self):
        pass

    def delete(self):
        pass


def make_app():
    return Application([
        ('/user', LoginHandler)
    ],
        default_host=options.h)

if __name__ == '__main__':
    define('p', default=7000, type=int, help='绑定端口')
    define('h', default='localhost', type=str, help='主机地址')
    parse_command_line()   # 解析命令行

    app = make_app()
    app.listen(options.p)

    print('Running http://%s:%s' % (options.h, options.p))
    IOLoop.current().start()