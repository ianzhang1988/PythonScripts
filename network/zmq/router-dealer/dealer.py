#coding=utf-8
from __future__ import print_function
import zmq
import random
import time,sys
PY3 = sys.version_info[0] == 3

name = sys.argv[1]
print(type(name))
#name = name.encode('utf-8')

context = zmq.Context()
worker = context.socket(zmq.DEALER)
if PY3:
    worker.setsockopt_string(zmq.IDENTITY, name)
else:
    worker.setsockopt(zmq.IDENTITY, name)

worker.connect("ipc:///tmp/zmqtest/routertest")

total = 0
while True:
    # We receive one part, with the workload
    request = worker.recv()
    print(request)
    finished = request == b"END"
    if finished:
        print("A received: %s" % total)
        break
    total += 1
    if total % 3 == 0:
        worker.send(('greetings from %s' % name).encode('utf-8'))
