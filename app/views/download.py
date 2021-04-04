from tornado import gen
from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import HTTPClient, HTTPResponse
from tornado.httpclient import AsyncHTTPClient


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


class AsyncDownloadHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        filename = self.get_query_argument('filename', 'index.html')

        from app import BASE_DIR, os

        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.finish()
    @asynchronous
    def get(self):
        url = self.get_query_argument('url')

        # 异步请求
        client = AsyncHTTPClient()
        response: HTTPResponse =client.fetch(url, self.save, validate_cert=False)

        self.write('下载中')


class AsyncHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        filename = self.get_query_argument('filename', 'index.html')

        from app import BASE_DIR, os

        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('下载成功')
        self.finish()
    @asynchronous
    async def get(self):
        url = self.get_query_argument('url')

        self.write('下载中')
        # 异步请求
        client = AsyncHTTPClient()
        response = await client.fetch(url, validate_cert=False)

        self.save(response)
        self.set_status(200)