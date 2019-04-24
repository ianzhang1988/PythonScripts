# coding=utf-8
from __future__ import print_function
import zmq
import random
import time

context = zmq.Context()
router = context.socket(zmq.ROUTER)
# router.setsockopt(zmq.ROUTER_MANDATORY, 1) # cause exception need investigation
router.bind("ipc:///tmp/zmqtest/routertest")

# Send 10 tasks scattered to A twice as often as B
for i in range(1000):
    # Send two message parts, first the address…
    ident = random.choice(['A', 'A', 'B'])
    # And then the workload
    work = b"This is the workload %s" % i
    print('sending')
    router.send_multipart([ident, work])

    print('receiving')
    try:
        parts = router.recv_multipart(flags=zmq.NOBLOCK)
        print(parts)
    except zmq.error.Again:
        pass

    time.sleep(0.5)

router.send_multipart(['A', 'END'])
router.send_multipart(['B', 'END'])

