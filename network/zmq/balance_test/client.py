# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 15:59
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from __future__ import print_function
import sys

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:4501")

#  Do 10 requests, waiting each time for a response
for request in range(100):
    print("Sending request %s …" % request)
    socket.send_json({'counter':request})

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

# 这种方式是“同步的”，每次去到时间长的worker的可能性都是一样的。所以就很慢