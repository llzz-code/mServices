
from tornado.web import RequestHandler
from tornado.httpclient import HTTPClient, HTTPResponse


class DownloadHandler(RequestHandler):
    def get(self):
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename', 'index.html')
        client = HTTPClient()
        response: HTTPResponse = client.fetch(url, validate_cert=False)
        # print(response.body)

        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('下载成功')