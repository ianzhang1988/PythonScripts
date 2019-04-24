# coding=utf-8
import zmq
import threading
import time

class Client():
    def __init__(self):
        self.threads = []
        self.count = 100
        self.context = zmq.Context()
        self.sockets = []

    def start(self):

        for i in range(5):
            # bad idea for thread safety
            # sock = self.context.socket(zmq.REQ)
            # self.sockets.append(sock)
            # sock.setsockopt(zmq.SNDTIMEO, 1000)
            # sock.connect('tcp://127.0.0.1:6666')
            # sock.connect('tcp://127.0.0.1:6667')
            thread = threading.Thread(target=self.perf, args=(i,))
            thread.start()
            self.threads.append(thread)

    def perf(self, id):
        # good idea for thread safety
        sock = self.context.socket(zmq.REQ)
        sock.setsockopt(zmq.SNDTIMEO, 1000)
        sock.connect('tcp://127.0.0.1:6666')
        sock.connect('tcp://127.0.0.1:6667')

        count = 100000
        begin = time.time()
        for i in range(count):
            sock.send_json({"content":'hi from client %s, count %s' % (id, i)})
            content = sock.recv_json()

        time_use = time.time() - begin

        sock.setsockopt(zmq.LINGER, 0)
        sock.close()
        print( 'client %s finished, use %ss, avg %s'% (id, time_use,  time_use/count) )


    def work(self, id):
        sock = self.context.socket(zmq.REQ)
        sock.setsockopt(zmq.SNDTIMEO, 1000)
        sock.connect('tcp://127.0.0.1:6666')
        sock.connect('tcp://127.0.0.1:6667')

        count = self.count
        for i in range(count):
            sock.send_json({"content":'hi from client %s, count %s' % (id, i)})

            content = sock.recv_json()
            print('echo',content)
            time.sleep(1)

        sock.setsockopt(zmq.LINGER, 0)
        sock.close()

    def close(self):
        # for sock in self.sockets:
        #     sock.setsockopt(zmq.LINGER, 0)
        #     sock.close()

        self.context.term()

def main():
    c = Client()
    c.start()
    time.sleep(300)

if __name__ == '__main__':
    main()

