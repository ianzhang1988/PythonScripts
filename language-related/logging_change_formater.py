# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 15:06
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com
import logging, os, uuid
import logging.handlers
import threading, time

MODULE='test'
work_flag = True

class LoggingConfig:
    def __init__(self):
        self.log_id = 'something'
        self.fh = None
        self.sh = None
        self.log_file = None
        self.log_path = None

    def init_logging(self):
        # hostname = socket.gethostname()
        # log_file = MODULE + "." + hostname + "." + str(pool) + ".log"
        self.log_file = MODULE + ".log"
        logger = logging.getLogger()
        logger.setLevel('DEBUG')

        #create log path
        self.log_path = "."
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        self.fh = logging.handlers.TimedRotatingFileHandler(os.path.join(self.log_path, self.log_file), when='D', backupCount=3)
        self.sh = logging.StreamHandler()

        formatter = logging.Formatter(
            'ugc-worker {} {} %(asctime)s %(module)s:%(filename)s L%(lineno)d %(levelname)s: %(message)s'.format(
                self.log_id,
                os.getenv('MY_POD_NAME', str(uuid.uuid4()))
            )
        )
        self.fh.setFormatter(formatter)
        self.sh.setFormatter(formatter)

        logger.addHandler(self.fh)
        logger.addHandler(self.sh)

        logging.info("Current log level is : %s",logging.getLevelName(logger.getEffectiveLevel()))

    def change_log_id(self, id):
        self.log_id = id

        formatter = logging.Formatter(
            'ugc-worker {} {} %(asctime)s %(module)s:%(filename)s L%(lineno)d %(levelname)s: %(message)s'.format(
                self.log_id,
                os.getenv('MY_POD_NAME', str(uuid.uuid4()))
            )
        )
        self.fh.acquire()
        self.fh.setFormatter(formatter)
        self.fh.release()

        self.sh.acquire()
        self.sh.setFormatter(formatter)
        self.sh.release()

def logging_working():
    counter = 0
    while work_flag:
        logging.info('%s', counter)
        counter+=1
        time.sleep(0.5)

def main():
    lc = LoggingConfig()
    lc.init_logging()

    t = threading.Thread(target=logging_working)
    t.start()

    for i in range(10):
        time.sleep(1)
        lc.change_log_id('id_%s' % i)

    global work_flag
    work_flag = False
    t.join()

if __name__ == '__main__':
    main()