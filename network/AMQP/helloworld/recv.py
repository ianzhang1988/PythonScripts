# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:39
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('10.19.17.188'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('%s %s %s' %(ch,method, properties))
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

