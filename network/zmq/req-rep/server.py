# coding=utf-8
from __future__ import print_function
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc:///tmp/zmqtest/0")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Send reply back to client
    socket.send(b"")