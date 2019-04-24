# coding=utf-8

import mmap
import multiprocessing
import time

def read_process(id):
    f = open('share_file', 'r+b')
    mapf = mmap.mmap(f.fileno(), 0)

    for i in range(100):
        print(mapf[:])
        #print(mapf.read(20))
        #mapf.seek(0)
        time.sleep(1)

    mapf.close()
    f.close()

if __name__ == '__main__':
    p_pool = []
    for i in range(3):
        p = multiprocessing.Process(target=read_process, args=(i,))
        p_pool.append(p)
        p.start()

    for p in p_pool:
        p.join()
