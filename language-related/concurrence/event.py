# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 16:12
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from threading import Thread, Event

g_event = None

def thread1():
    g_event.wait()
    print('thread 1')

def thread2():
    g_event.wait()
    print('thread 2')

def main():
    global  g_event
    g_event = Event()

    t1 = Thread(target=thread1)
    t1.start()

    t2 = Thread(target=thread2)
    t2.start()

    g_event.set()


if __name__ == '__main__':
    main()