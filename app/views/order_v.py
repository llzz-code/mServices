from tornado.web import RequestHandler


class OrderHandler(RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'Python3',
            'author': 'lz',
            'price': 100
        },
        {
            'id': 2,
            'name': 'Python2',
            'author': 'lz',
            'price': 150
        }
    ]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }
    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def initialize(self):
        # 所有请求方法再调用前，都会进行初始化
        print('------initialize----')

    def prepare(self):
        # 在预处理之后，在行为方法之前
        print('--------prepare-----')
        # 主要用于验证参数、权限、读取缓存

    def on_finish(self):
        # 在请求行为方法之后，释放资源
        print('---finish----')




    def get(self, order_id, action_code):
        html = """
            <p>
                商品编号: %s
            </p>
            <p>
                商品名称: %s
            </p>
            <p>
                商品价格: %s
            </p>
        """
        goods = self.query(int(order_id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(action_code)))



