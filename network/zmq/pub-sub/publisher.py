#coding=utf-8
from __future__ import print_function
import zmq
from random import choice
import json,time
import queue,threading

context = zmq.Context()
socket = context.socket(zmq.PUB)
#socket.bind("ipc:///tmp/zmqtest/pubsubtest")
socket.bind("tcp://127.0.0.1:8765")

q = queue.Queue(10)

# def read_input(q):
#     while True:
#         try:
#             input_str = input('input ')
#             print(input_str,type(input_str))
#             id,cmd = input_str.split(' ')
#             q.put((int(id),cmd))
#         except Exception as e:
#             print('input error:%s'%e)
#
# t = threading.Thread(target=read_input,args=(q,))
# t.start()

q.put((1,'test'))
q.put((2,'test2'))

counter=0
while True:
    counter+=1
    zipcode = choice((1,2))
    content = json.dumps(
        {'id': '%05d' % zipcode, '1': 'this', '2': 'is', '3': 'a test for %s' % zipcode, 'counter': counter})
    try:
        id, cmd = q.get(block=False)
        if cmd == 'exit':
            break
        content = json.dumps({'cmd':cmd})
        zipcode = id
    except queue.Empty:
        pass
    time.sleep(0.5)
    # socket.send_string(("%05d %s" % (zipcode,content)))
    socket.send_multipart(( ('%05d'%zipcode).encode('utf-8'), content.encode('utf-8')))

    #socket.send_string("%s" %  content)