# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 15:42
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import zmq
import time
import threading

class Proxy():
    def __init__(self):
        pass

    def setup_test(self):

        t1 = threading.Thread(target=self.worker, args=(1,))
        t1.start()
        t2 = threading.Thread(target=self.worker, args=(2,))
        t2.start()

        self.proxy()

    def proxy(self):
        context = zmq.Context()

        front_end = context.socket(zmq.ROUTER)
        back_end = context.socket(zmq.DEALER)
        #back_end.setsockopt(zmq.SNDHWM, 5)
        back_end.set_hwm(1)
        """
        hwm还和网络上的缓存等环境情况有关，所以他并不适合作为一个控制阈值
        他就是用来限制内存使用量的阈值
        the real HWM is SNDHWM + RCVHWM + X, where X is dependent on a lot of factors
        """
        front_end.bind('tcp://127.0.0.1:4501')
        back_end.bind('tcp://127.0.0.1:4502')
        print('hwm',back_end.get_hwm())

        # try:
        #     zmq.proxy(front_end, back_end)
        # except zmq.ContextTerminated:
        #     print('context close')

        poller = zmq.Poller()
        print('zmq.POLLIN',zmq.POLLIN)
        print('zmq.POLLOUT', zmq.POLLOUT)
        poller.register(front_end,flags=zmq.POLLIN)
        poller.register(back_end,flags=zmq.POLLIN)

        while True:
            poll_list = poller.poll()

            for (socket,event) in poll_list:
                if socket is front_end and event == zmq.POLLIN:
                    print('front_end',event)

                    content = front_end.recv_multipart()
                    # id, '', 数据
                    print(content)
                    if not context:
                        print('connect break')
                        break
                    back_end.send_multipart(content)
                    """
                    发送出去时的结构是 '',id, '', 数据
                    到了REQ时， REQ自动把'',id, '',拿下来保存起来，send的时候再把'',id, '',套回去
                    """

                if socket is back_end and event == zmq.POLLIN:
                    print('back_end',event)

                    content = back_end.recv_multipart()
                    print(content)
                    if not context:
                        print('connect break')
                        break
                    front_end.send_multipart(content)

        front_end.close()
        back_end.close()

    def worker(self,id):
        context = zmq.Context()
        receiver = context.socket(zmq.REP)
        """
        观察client，DEALER是严格的按照轮询的方式分发任务的
        worker这里使用REP的话，如果时间worker 1 总是处理长时间的任务，并且达到hwm，逻辑上的结果就是吧proxy阻塞
        所以REQ 和 REP 不能用来实现这种异步方式的负载均衡
        """
        #receiver.setsockopt(zmq.RCVHWM, 5)
        receiver.set_hwm(5)
        receiver.connect('tcp://127.0.0.1:4502')


        while True:
            content = receiver.recv_json()
            if not context:
                print('connection break id:%s' % id)
                break
            print(type(content),content)
            content[u'from']=u'work id: %s' % id
            print(content)
            receiver.send_json({ 'counter':content['counter'], 'from': 'work id: %s' % id})
            if id == 1:
                time.sleep(5)

        receiver.close()

if __name__ == '__main__':
    p = Proxy()
    p.setup_test()


