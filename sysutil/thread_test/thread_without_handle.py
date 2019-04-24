# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 18:18
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import threading
import time
import gc

class TestWith(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('%s exit'%self.name)


class TestThread(threading.Thread):

    def __init__(self, name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0

        threading.Thread.__init__(self, name=name)

    def run(self):
        """ main control loop """
        with TestWith(self.getName(  )) as _:
            print "%s starts" % (self.getName(  ),)

            count = 0
            while True:
                count += 1
                # print "loop %d" % (count,)
                # self._stopevent.wait(self._sleepperiod)
                if count > 10:
                    raise Exception('test')
                time.sleep(1)

            print "%s ends" % (self.getName(),)

    def join(self, timeout=None):
        """ Stop the thread. """
        print "%s join" % (self.getName(),)
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)

    def __del__(self):
        print('del called'%( self.getName(),))
        #super(TestThread, self).__del__()


class TestDel(object):
    def __del__(self):
        print('TestDel del')

if __name__ == "__main__":
    a = TestDel()
    del a

    for i in range(1):
        testthread = TestThread(name=str(i))
        # testthread.daemon = True
        testthread.start()

    #del testthread
    # gc.collect()

    time.sleep(100.0)

    # testthread.join()