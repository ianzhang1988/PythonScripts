# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 10:35
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import subprocess, os
import logging
import logging.handlers
import time

class HDFSError(Exception):
    pass

class HadoopFsAdapterClient(object):

    def __init__(self, hdfs_user_name, hdfs_root):
        self.hdfs_user_name = hdfs_user_name
        self.hdfs_root_path = hdfs_root

        os.environ['HADOOP_ROOT_LOGGER']="DEBUG,console"
        self.count = 0
        self.max_count = 100
        self.time_gap = [(10,30),(30,45), (45,60), (60, 99999999)]
        self.time_gap_prefix = ['20s','45s','60s','60up']

    def _run_shell(self, operation, operand):
        hadoop_bin = "/opt/hadoop-2.4.1/bin/hadoop"
        # cmd_tmp = 'runuser -l {user} -c "{hadoop_bin} fs -{operation} {operand}"'
        # su user, run python, otherwise no debug output
        cmd_tmp = "{hadoop_bin} fs -{operation} {operand}"

        cmd = cmd_tmp.format(user=self.hdfs_user_name, hadoop_bin=hadoop_bin, operation=operation, operand=operand)
        ret = 0

        begin = time.time()
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            ret = e.returncode
            output = e.output
            logging.error('check_output error: %s', str(e))

        time_elapsed = time.time() - begin

        if ret == 0 :
            self.record_abnormal_case(time_elapsed, output)

        logging.info('hdfs cmd: %s, ret: %s, time: %s', cmd, ret, time_elapsed)


        return True if ret == 0 else False

    def record_abnormal_case(self, time_elapsed, output):

        if time_elapsed < 10:
            return

        for idx, (lo,hi) in enumerate(self.time_gap):
            if time_elapsed > lo and time_elapsed <= hi:
                break

        prefix = self.time_gap_prefix[idx]

        with open('%s_%04d_%04d.txt' % (prefix, int(time_elapsed), self.count), 'w') as f:
            f.write(output)

        self.count+=1

    def if_continue(self):
        return self.count < self.max_count


    def upload(self, local_path, hdfs_path):
        # make hdfs parent path
        hdfs_path = self.hdfs_root_path + '/' + hdfs_path
        hdfs_path = hdfs_path.rstrip('/')
        operation='mkdir -p'
        operand = os.path.dirname(hdfs_path)
        self._run_shell(operation, operand)

        operation='put -f'
        operand = '{local_path} {hdfs_path}'.format(local_path=local_path, hdfs_path=hdfs_path)
        ret = self._run_shell(operation, operand)

        # if not ret:
        #     raise HDFSError("upload hdfs error")
        # return ret

def main():
    # config logging
    log_file = "debug_hdfs.log"
    logger = logging.getLogger()
    logger.setLevel('DEBUG')

    # create log path
    log_path = '.'

    fh = logging.handlers.TimedRotatingFileHandler(os.path.join(log_path, log_file), when='D', backupCount=7)
    sh = logging.StreamHandler()

    ###########This set the logging level that show on the screen#############
    # sh.setLevel(logging.DEBUG)
    # sh.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        '%(asctime)s :%(filename)s L%(lineno)d %(levelname)s: %(message)s'
    )

    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(sh)
    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))


    client = HadoopFsAdapterClient('sohuvideo','/user/sohuvideo')

    while client.if_continue():
        client.upload('debug_hdfs', 'online/encodedFile')

if __name__ == "__main__":
    main()