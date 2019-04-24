# coding=utf-8
import zmq
import threading
import time
from multiprocessing.dummy import Value

class Client():
    def __init__(self):
        self.threads = []
        self.count = 20
        self.context = zmq.Context()
        self.value = Value('I', 0)
        self.value.value = 0

    def start(self):
        for i in range(5):
            thread = threading.Thread(target=self.perf, args=(i,))
            thread.start()
            self.threads.append(thread)

    def perf(self, id):
        # good idea for thread safety
        sock = self.context.socket(zmq.REQ)
        sock.setsockopt(zmq.SNDTIMEO, 1000)
        sock.connect('tcp://127.0.0.1:5555')

        count = 10000
        begin = time.time()

        for i in range(count):
            sock.send_json({"content":'hi from client %s, count %s' % (id, i)})
            content = sock.recv_json()

        time_use = time.time() - begin

        sock.setsockopt(zmq.LINGER, 0)
        sock.close()
        print( 'client %s finished, use %ss, avg %s'% (id, time_use,  time_use/count) )

    # test mem block send
    def perf2(self, id):
        # good idea for thread safety
        sock = self.context.socket(zmq.REQ)
        sock.setsockopt(zmq.SNDTIMEO, 1000)
        sock.connect('tcp://127.0.0.1:5555')

        data = '1' * 1980 * 1080 * 3

        count = 1000
        begin = time.time()
        for i in range(count):
            sock.send(data)
            content = sock.recv_json()

        time_use = time.time() - begin

        sock.setsockopt(zmq.LINGER, 0)
        sock.close()
        print('client %s finished, use %ss, avg %s' % (id, time_use, time_use / count))


    def work(self, id):
        sock = self.context.socket(zmq.REQ)
        sock.setsockopt(zmq.SNDTIMEO, 1000)
        sock.connect('tcp://127.0.0.1:5555')

        count = self.count
        for i in range(count):
            self.value.value += 1
            sock.send_json({"content":'hi from client %s, count %s' % (id, self.value.value)})

            content = sock.recv_json()
            print('echo',content)
            time.sleep(5)

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
    c.close()

if __name__ == '__main__':
    main()

