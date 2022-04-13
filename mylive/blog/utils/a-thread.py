# _*_ coding:utf-8 _*_

import threading
import time
number = 0
lock = threading.Lock()
def plus():
    global number

    for i in range(1000000):
        lock.acquire()
        number += 1
        lock.release()
for i in range(3):
    print(i)
    t = threading.Thread(target=plus)
    t.start()
    print(threading.activeCount())
print(number)
while threading.activeCount() > 1:
    time.sleep(threading.activeCount())
print(number)

print('主线程结束')
