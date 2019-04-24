# coding=utf-8

import zmq
import threading
import time

class Server():
    def __init__(self):
        self.context = zmq.Context()

        self.working = True
        self.thread1 = None
        self.thread2 = None

    def start(self):
        # bad idea for thread safety
        # self.server_sock1 = self.context.socket(zmq.REP)
        # self.server_sock2 = self.context.socket(zmq.REP)
        # self.server_sock1.setsockopt(zmq.RCVTIMEO, 1000)
        # self.server_sock2.setsockopt(zmq.RCVTIMEO, 1000)
        # self.server_sock1.bind('tcp://127.0.0.1:6666')
        # self.server_sock2.bind('tcp://127.0.0.1:6667')

        self.working = True
        self.thread1 = threading.Thread(target=self.work, args=(1,))
        self.thread2 = threading.Thread(target=self.work, args=(2,))
        self.thread1.start()
        self.thread2.start()


    def work(self, thread_id):
        server_sock = None
        # good idea for thread safety
        server_sock = self.context.socket(zmq.REP)
        server_sock.setsockopt(zmq.RCVTIMEO, 1000)
        if thread_id == 1:
            server_sock.bind('tcp://127.0.0.1:6666')
        else:
            server_sock.bind('tcp://127.0.0.1:6667')

        while self.working:
            content = None
            try:
                content = server_sock.recv_json()
            except zmq.Again:
                continue

            # echo back
            if content is not None:
                content['server_id'] = thread_id

            server_sock.send_json(content)

            print('thread %s:'%thread_id, content)

        server_sock.setsockopt(zmq.LINGER, 0)
        server_sock.close()

    def close(self):
        self.working = False

        # self.server_sock1.setsockopt(zmq.LINGER, 0)
        # self.server_sock2.setsockopt(zmq.LINGER, 0)

        self.thread1.join()
        self.thread2.join()

        # self.server_sock1.close()
        # self.server_sock2.close()

        self.context.term()

def main():
    s = Server()
    s.start()
    time.sleep(300)
    s.close()

if __name__ == '__main__':
    main()