# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 15:44
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from threading import Event
import threading
import time

class GlobalVar:
    kill_task_flag=Event()

def kill_task():
    GlobalVar.kill_task_flag.set()

def thread():
    print('flag', GlobalVar.kill_task_flag.is_set())
    time.sleep(1)
    print('flag', GlobalVar.kill_task_flag.is_set())

t = threading.Thread(target=thread)
t.start()

kill_task()

t.join()