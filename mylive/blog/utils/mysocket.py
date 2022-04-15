# _*_ coding:utf-8 _*_
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
s.bind((ip, 8008))
s.listen(3)
while 1:
    conn, addr = s.accept()
    print(addr)
    while 1:
        data = conn.recv(1024)
        if len(data) == 0:
            print('结束当前连接')
            break
        print(data.decode('utf-8'))
        conn.sendall('你好'.encode('utf-8'))

    conn.close()
