# coding=utf-8

import zmq
import threading
import time

class ProxyServer():
    def __init__(self):
        self.context = zmq.Context()
        self.context2 = zmq.Context()
        self.working = False

    def start(self):
        self.working = True
        frontend = self.context.socket(zmq.ROUTER)
        backend = self.context.socket(zmq.DEALER)
        frontend.bind("tcp://*:5555")
        #backend.bind('inproc://workers')
        backend.bind('tcp://*:5556')

        self.thread1 = threading.Thread(target=self._work, args=(1,))
        self.thread2 = threading.Thread(target=self._work, args=(2,))
        self.thread1.start()
        self.thread2.start()

        try:
            zmq.proxy(frontend, backend)
        except zmq.ContextTerminated:
            print('context close')

        frontend.close()
        backend.close()

    def _work(self, id):
        #server_sock = self.context2.socket(zmq.REP)
        server_sock = self.context2.socket(zmq.REP)
        # server_sock.connect('inproc://workers')
        server_sock.connect('tcp://127.0.0.1:5556')
        server_sock.setsockopt(zmq.RCVTIMEO, 1000)

        while self.working:
            content = None
            try:
                #content = server_sock.recv_json()
                content = server_sock.recv_json()
            except zmq.Again:
                continue

            # echo back
            if content is not None:
                content['server_id'] = id

            server_sock.send_json(content)

            # print('thread %s:'%id, content)

        server_sock.setsockopt(zmq.LINGER, 0)
        server_sock.close()

    # test mem block send
    def _work2(self, id):
        #server_sock = self.context2.socket(zmq.REP)
        server_sock = self.context2.socket(zmq.REP)
        # server_sock.connect('inproc://workers')
        server_sock.connect('tcp://127.0.0.1:5556')
        server_sock.setsockopt(zmq.RCVTIMEO, 1000)

        while self.working:
            content = None
            try:
                #content = server_sock.recv_json()
                content = server_sock.recv()
            except zmq.Again:
                continue

            # echo back
            rep_body ={}
            rep_body['server_id'] = id
            rep_body['recv_len'] = len(content)

            server_sock.send_json(rep_body)

            # print('thread %s:'%id, content)

        server_sock.setsockopt(zmq.LINGER, 0)
        server_sock.close()

    def close(self):
        self.working = False

        print('close')
        self.context.term()
        print('term')

        self.thread1.join()
        self.thread2.join()
        self.context2.term()

def main():
    s = ProxyServer()
    t = threading.Thread(target=s.start)
    t.start()
    time.sleep(300)
    s.close()
    t.join()

if __name__ == '__main__':
    main()