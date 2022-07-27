# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 12:27
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import sys
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(100):
    message='worker [%s] %s' % (i,"."*random.randint(1,5))

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)

    time.sleep(1)

connection.close()
