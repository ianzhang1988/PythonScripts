# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 10:46
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import threading
import time

def test():
    print('thread begin')
    time.sleep(10)
    print('thread end')

def main():

    t = threading.Thread(target=test)

    try:
        t.start()
        time.sleep(1)
        raise Exception()
        t.join()

    except Exception as e:
        pass

    print('before main return')


if __name__ == '__main__':
    main()
    print('after main return')