# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 12:18
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com
import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

for i in range(100):
    severity = random.sample(["info", "warning" ,"error"],1)[0]
    message = "i:%s %s" % (i, severity)

    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))

connection.close()