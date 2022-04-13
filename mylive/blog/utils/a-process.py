# _*_ coding:utf-8 _*_
import time, random
from multiprocessing import Process, Pool
import os
def piao(args):

    print(' start task %s (%s) at %s:' %(args, os.getpid(), time.strftime("%H:%M:%S")))
    time.sleep(random.randint(1,5))
    print(' end task %s (%s) at %s:' % (args, os.getpid(), time.strftime("%H:%M:%S")))
if __name__ == '__main__':
    print('cpu number is %s '%os.cpu_count())
    p = Pool(3)
    for i in range(5):
        p.apply_async(piao, args=(i,))
    p.close()
    p.join()
    p1 = Process(target=piao, args=('e',))
    p1.start()
