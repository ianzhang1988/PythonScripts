# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 12:28
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika
import time

import threading
import functools

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.19.17.188'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_qos(prefetch_count=1)

def ack_message(channel, delivery_tag, threads):
    """Note that `channel` must be the same pika channel instance via which
    the message being ACKed was retrieved (AMQP protocol constraint).
    """
    time.sleep(1)
    print("ack_message %s" % delivery_tag)
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        # Channel is already closed, so we can't ACK this message;
        # log and/or do something that makes sense for your app in this case.
        pass

    t = threads[delivery_tag]
    t.join()
    del threads[delivery_tag]

def do_work(connection, channel, delivery_tag,  body, threads):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    cb = functools.partial(ack_message, channel, delivery_tag, threads)
    connection.add_callback_threadsafe(cb)
    print("do_work %s"%delivery_tag)

def on_message(channel, method_frame, body, connection, threads):
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=do_work, args=(connection, channel, delivery_tag, body, threads))
    t.start()
    threads[delivery_tag] = t

threads = {}

for method, properties, body in channel.consume('task_queue', inactivity_timeout=1):

    if not method:
        continue

    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    on_message(channel, method, body, connection, threads)

    print("thread num %s" % len(threads))

# Wait for all to complete
for thread in threads.values():
    thread.join()

connection.close()