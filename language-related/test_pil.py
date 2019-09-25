# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 14:34
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com
import time
import os
import threading

def count_down(n):
    while True:
        print(n)
        n -= 1
        if n < 1:
            break
        time.sleep(1)

def test_gil():
    time.sleep(3)
    print('system sleep')
    #os.system('ping 127.0.0.1 -n 10 > nul')
    os.system('sleep 10')
    print('system sleep end')

def main():
    t1 = threading.Thread(target=count_down,args=(30,))
    t2 = threading.Thread(target=test_gil)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

# so block in one thread will no block other thread, which means
# that block would not affect gil
