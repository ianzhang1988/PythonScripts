# coding=utf-8

import mmap
import time
import struct

f = open('share_file','w+b')
size = 1920*1080*3 + 4
f.seek(size-1)
f.write(b'0')
f.close()

data = '1'*1920*1080*3

f = open('share_file','r+b')
mapf = mmap.mmap(f.fileno(), size)

content_item = 'abcdefgh'

write_counter = 0
read_counter = 12345

for _ in xrange(1000):
    for i in content_item:
        mapf[4:] = data
        mapf[4:10] = i*6
        mapf[:2] = struct.pack('H',write_counter)

        #write_counter += 1
        # while True:
        #     tmp_counter = struct.unpack('H', mapf[2:4])
        #     if tmp_counter == read_counter:
        #         time.sleep(0.00001)
        #     elif tmp_counter == read_counter + 3:
        #         read_counter = tmp_counter
        #         print(read_counter)
        #         break
        #     else:
        #         time.sleep(0.00001)

        time.sleep(0.00001)
mapf.close()
f.close()