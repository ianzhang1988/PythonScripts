# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 12:22
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com


from kazoo.client import KazooClient
import time

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

for i in range(100):
    try:
        time.sleep(1)
        r = zk.get("/testloss")
        print(r[0])
    except Exception as e:
        print(e)

zk.stop()