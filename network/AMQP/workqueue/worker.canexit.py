# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 16:50
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import time
import signal

work_flag = True

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_qos(prefetch_count=1)

def close(sig, frame):
    global work_flag
    print('connection close')
    # channel.stop_consuming()
    work_flag = False

signal.signal(signal.SIGTERM, close)
signal.signal(signal.SIGINT, close)


for method, properties, body in channel.consume('task_queue', inactivity_timeout=1):
    if not work_flag:
        break

    if not method:
        continue

    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    channel.basic_ack(method.delivery_tag)



