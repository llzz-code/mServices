import socket



# 1、创建socket
socket = socket.socket()

# 2、连接服务器
socket.connect(('localhost', 7000))
socket.send('connect'.encode('utf-8'))

# 3、接收数据
msg = socket.recv(4096)
print('Server:', msg.decode('utf-8'))

# 4、向服务端发送数据
socket.send('你好，Server'.encode('utf-8'))

# 5、关闭
socket.close()