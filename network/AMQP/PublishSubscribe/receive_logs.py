# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 18:18
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.19.17.188'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# queue='' random queue from server, exclusive=True queue auto close
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()