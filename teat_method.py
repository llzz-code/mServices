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
