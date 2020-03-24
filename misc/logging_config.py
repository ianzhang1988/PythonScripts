# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 11:51
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import logging
import logging.handlers
import socket
import os

# hostname = socket.gethostname()
log_file = "test.log"
logger = logging.getLogger()
logger.setLevel('DEBUG')

#create log path
log_path = '.'

fh = logging.handlers.TimedRotatingFileHandler(os.path.join(log_path, log_file), when='D', backupCount=7)
sh = logging.StreamHandler()

###########This set the logging level that show on the screen#############
#sh.setLevel(logging.DEBUG)
#sh.setLevel(logging.ERROR)

formatter = logging.Formatter(
    '%(asctime)s :%(filename)s L%(lineno)d %(levelname)s: %(message)s'
)

fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)
logging.info("Current log level is : %s",logging.getLevelName(logger.getEffectiveLevel()))