from tornado.web import UIModule


class NavModule(UIModule):
    def render(self):
        data = {
            'navs': {
                    '管理员列表': 'admin/index',
                    '博客中心': 'blog/index',
                    '新闻中心': 'news/index',
                    '监测中心': 'monitor/index'
                }
        }

        return self.render_string('ui/nav.html', **data)




