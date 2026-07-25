"""
import socket
server = socket.socket() # 1. 新建socket
server.bind(('127.0.0.1', 8999)) # 2. 绑定IP和端口（其中127.0.0.1为本机回环IP）
server.listen(5) # 3. 监听连接
s, addr = server.accept() # 4. 接受连接
print('connect addr：{}'.format(addr))
content =s.recv(1024)
print(str(content, encoding='utf-8'))  # 接受来自客户端的消息，并编码打印出来
s.close()
"""
import socket

server = socket.socket() # 1. 新建socket
server.bind(('127.0.0.1', 8999)) # 2. 绑定IP和端口（其中127.0.0.1为本机回环IP）
server.listen(5) # 3. 监听连接
s, addr = server.accept() # 4. 接受连接
print('connect addr：{}'.format(addr))
while True:
    content =s.recv(1024)
    if len(content) == 0:
        break
    s.send(content)
    print(str(content, encoding='utf-8')) # 接受来自客户端的消息，并打印出来

s.close()

"""
Python自带的HTTP服务器，默认的端口为8000端口，同时默认的目录是当前终端启动运行的目录，请启动Python自带的HTTP服务器，指定端口为9999，并指定目录路径为C:/。

?不会了怎么办
1. 请同学在本地编写代码练习；

2. 通过-d命令可以指定目录路径。

参考答案：

python -m http.server 9999 -d C:/
"""