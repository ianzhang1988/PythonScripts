#coding=utf-8
from __future__ import print_function
import zmq

context = zmq.Context()

socket = context.socket(zmq.SERVER)
socket.bind("127.0.0.1:5555")

while True:
    message = socket.recv()
    print("Received request: %s" % message)



