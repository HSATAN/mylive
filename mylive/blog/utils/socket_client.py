# _*_ coding:utf-8 _*_
import socket
import requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostbyname(socket.gethostname()), 8008))
s.connect(('49.235.125.109', 8008))
s.send('我是客户端'.encode('utf-8'))
data = s.recv(1024)
print(data.decode('utf-8'))
s.close()