import json

from tornado.web import RequestHandler


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
