#coding=utf-8
from __future__ import print_function
import sys
import zmq
import json
PY3 = sys.version_info[0] == 3

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server…")
# socket.connect("ipc:///tmp/zmqtest/pubsubtest")
socket.connect("tcp://127.0.0.1:8765")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = '%05d' % int(sys.argv[1])
if not PY3:
    zip_filter = zip_filter.decode('utf-8')

# Python 2 - ascii bytes to unicode str
# if isinstance(zip_filter, bytes):
#     zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
socket.RCVTIMEO = 1000

# Process 5 updates
total_temp = 0
# while True:
#     try:
#         string = socket.recv_string()
#     except zmq.error.Again:
#         print('zmq.error.Again')
#         continue
#     # print(string)
#     content = json.loads( string[6:] )
#     print(content)
#     if 'cmd' in content and content['cmd'] == 'quit':
#         print('quiting')
#         break

while True:
    try:
       id, string = socket.recv_multipart()
    except zmq.error.Again:
        print('zmq.error.Again')
        continue
    # print(string)
    content = json.loads( string )
    print(content)
    if 'cmd' in content and content['cmd'] == 'quit':
        print('quiting')
        break



print('finished')



