# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 17:16
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import os
import threading
import multiprocessing
import time

def run_thread(path):
    os.chdir(path)
    time.sleep(2)
    f = open('%s.txt'%path,'w')
    f.write(path)
    f.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread,args=('./t1',))
    t2 = threading.Thread(target=run_thread, args=('./t2',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 2 file end up both in one folder, Process would work as expected(code shown below)

    # t1 = multiprocessing.Process(target=run_thread,args=('./t1',))
    # t2 = multiprocessing.Process(target=run_thread, args=('./t2',))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

