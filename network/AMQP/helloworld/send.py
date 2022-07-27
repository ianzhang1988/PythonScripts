# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:27
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()