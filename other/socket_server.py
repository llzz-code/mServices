import socket



# 1、创建socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、绑定host和port端口
server.bind(('localhost', 7000))

# 3、监听
server.listen()

# 4、等待接收客户端的连接
print('服务器已经启动')
client, address = server.accept()     # 阻塞的方法
print('%s 已连接' % address[0])
msg = client.recv(0)
print(msg.decode('utf-8'))
# 5、向客户端发送消息
client.send('你好，很高心认识你'.encode('utf-8'))

# 6、等待客户端发来消息
msg = client.recv(4096)    # 阻塞
print(address, '说：', msg.decode())

# client.close()
# server.close()








