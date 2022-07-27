# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 12:23
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# severities = sys.argv[1:]
# if not severities:
#     sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
#     sys.exit(1)

severities = random.sample(["info", "warning" ,"error"],2)
print("severities",severities)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()