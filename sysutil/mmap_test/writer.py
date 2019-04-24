# coding=utf-8

import mmap
import time

f = open('share_file','w+b')
size = 20
f.seek(size-1)
f.write(b'0')

mapf = mmap.mmap(f.fileno(), size)

content_item = 'abcdefgh'

for _ in xrange(100):
    for i in content_item:
        mapf[:] = i*size
        time.sleep(1)

mapf.close()
f.close()