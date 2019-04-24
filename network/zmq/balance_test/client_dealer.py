# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 15:59
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from __future__ import print_function
import sys
import json

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.DEALER)
socket.connect("tcp://127.0.0.1:4501")

#  Do 10 requests, waiting each time for a response
for request in range(100):
    print("Sending request %s …" % request)
    socket.send_multipart(['',json.dumps({'counter':request})])
    """
    REQ比DEALER自动加上了 ''这个分割符，自己使用的时候要回忆起来这个要点
    """


#  Get the reply.
print ('get reply')
for request in range(100):
    #message = socket.recv_json()
    message = socket.recv_multipart()
    print("Received reply %s [ %s ]" % (request, message))
