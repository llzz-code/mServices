from tornado.web import RequestHandler


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