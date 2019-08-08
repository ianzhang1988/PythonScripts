# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 15:22
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.19.17.188'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

for i in range(100):
    severity = random.sample(["info", "warning" ,"error"],1)[0]
    facility = random.sample(["foo", "bar", "baz"], 1)[0]
    routing_key = '.'.join([facility,severity])
    message = "i:%s %s" % (i, routing_key)

    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))


connection.close()