# Tornado实现的微服务
## 1、基本使用

```python
# 获取参数
# self.get_arguments('参数名')
# self.get_query_arguments('参数') 查询参数
# request 请求中的数据，返回dict类型，key对应的value为字节类型
# req: HTTPServerRequest = self.request
# req.arguments.get
```