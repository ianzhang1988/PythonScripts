# coding=utf-8
from __future__ import print_function
import sys
name = sys.argv[1]

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.CLIENT)
socket.connect("127.0.0.1:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10000000):
    print("Sending request %s …" % request)
    socket.send((name+" Hello").encode('utf-8'))

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))