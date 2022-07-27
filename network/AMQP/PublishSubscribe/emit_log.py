# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 18:15
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import sys
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

# no channel.queue_declare
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#message = ' '.join(sys.argv[1:]) or "info: Hello World!"

for i in range(100):
    message='worker [%s] %s' % (i,"."*random.randint(1,5))

    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(1)

connection.close()
