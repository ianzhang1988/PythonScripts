import threading
import time

def threadfunc():
    while True:
        time.sleep(1)
        print('thread runing')

th = threading.Thread(target=threadfunc)
th.daemon = True
th.start()
print('exit')