# coding=utf-8

import mmap
import multiprocessing
import time
import struct

def read_process(id):
    f = open('share_file', 'r+b')
    mapf = mmap.mmap(f.fileno(), 0)

    write_counter = 12345
    read_counter = 0

    counter = 0
    last=''

    begin = time.time()
    while True:

        # while True:
        #     tmp_counter = struct.unpack('H', mapf[:2])
        #     if tmp_counter == write_counter:
        #         time.sleep(0.00001)
        #     else:
        #         write_counter = tmp_counter
        #         print(write_counter)
        #         break


        if last != mapf[4:10]:
            last = mapf[4:10]
            counter+=1
        if counter > 1000:
            break

        # read_counter += 1
        # mapf[2:4] = struct.pack('H', read_counter)

    print(counter)
    print('time', time.time()-begin)

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
