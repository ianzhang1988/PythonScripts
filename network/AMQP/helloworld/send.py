# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:27
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('10.19.17.188', 5673))
channel = connection.channel()

channel.queue_declare(queue='hello')

ret = channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print("publish returned:", ret)
print(" [x] Sent 'Hello World!'")

connection.close()

