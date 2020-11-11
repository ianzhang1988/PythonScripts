# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:27
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('10.19.17.188', 5673))
channel = connection.channel()

channel.queue_declare(queue='hello')

msg_num = 3000

start = time.time()

for _ in range(msg_num):

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

print("not confirm time", time.time()-start)


start = time.time()

channel2 = connection.channel()
channel2.queue_declare(queue='hello')
channel2.confirm_delivery()

for _ in range(msg_num):

    channel2.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

print("with confirm time", time.time()-start)

connection.close()