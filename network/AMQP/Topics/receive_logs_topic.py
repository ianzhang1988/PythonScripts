# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 15:24
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.19.17.188'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# binding_keys = sys.argv[1:]
# if not binding_keys:
#     sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
#     sys.exit(1)

severity = random.sample(["info", "warning", "error",'*','#'], 1)[0]
facility = random.sample(["foo", "bar", "baz",'*','#'], 1)[0]
binding_keys = ['.'.join([facility, severity]),]
print("binding_keys",binding_keys)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()