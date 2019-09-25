# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 16:40
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.19.17.188'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.exchange_declare(exchange='my-exchange', exchange_type='x-delayed-message')

message = 'delayed hi!'

header = {'x-delay': 1000}
channel.basic_publish(
        exchange='my-exchange', routing_key='hello',properties=pika.BasicProperties(headers=header), body=message)
print(" [x] Sent :%s" %  (message,))


connection.close()