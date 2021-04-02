from unittest import TestCase
import requests

class TeatTornadoRequest(TestCase):
    base_url = 'http://localhost:7000'

    def test_index_get(self):
        url = self.base_url + '/'
        resp = requests.get(url, params={
            'name': 'lz',
            'city': 'JiangXi'
        })
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/'
        resp = requests.post(url, data={
            'name': 'lz',
            'city': 'JiangXi'
        })
        print(resp.text)


class TestUserRequset(TestCase):
    url = 'http://localhost:7000/user'

    def test_login(self):
        resp = requests.get(self.url,
                            json={
                                'name': 'lz',
                                'pwd': '123456'
                            })
        print(resp.text)