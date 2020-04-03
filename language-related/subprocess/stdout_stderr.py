# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 14:34
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import logging
import subprocess, os, sys
import time
import signal
from io import StringIO, TextIOWrapper, BytesIO

import re

class FFmpeg:
    def __init__(self, file_logger, time_out=3600*24):
        self.process = None
        self.output = None
        self.file_logger = file_logger
        self.timeout = time_out

        self.output = StringIO(newline='\n')

    def trans(self, trans_cmd):
        #self._trans_poll(trans_cmd)
        #self._trans_communicate(trans_cmd)
        #self._trans_read(trans_cmd)
        self._trans_new_stream(trans_cmd)

    def _trans_poll(self, trans_cmd):

        self.file_logger.info('FFmpeg run [%s]', trans_cmd)
        self.process = subprocess.Popen(trans_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            ret = self.process.poll()
            if ret != None:
                if ret != 0:
                    print('error')

                print('finished')
                break

            time.sleep(0.1)

            print('---')
            # here was blocked
            print(self.process.stdout.read().decode('gb2312'))

    def _trans_communicate(self, trans_cmd):

        self.file_logger.info('FFmpeg run [%s]', trans_cmd)
        self.process = subprocess.Popen(trans_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            try:
                (stdout, stderr) = self.process.communicate(timeout=1)
            except subprocess.TimeoutExpired as e:
                print('---')

                # here was blocked
                # print(self.process.stdout.read().decode('gb2312'))

                # print(e.stdout) # None
                # print(e.stderr) # None

                ## not working either
                # buffer_size = 1024
                # buffer = StringIO()
                # while True:
                #     print('------- 1')
                #     read_tmp = self.process.stdout.read(buffer_size)
                #     print('------- 2')
                #     buffer.write(read_tmp.decode('gb2312'))
                #     if len(read_tmp) < buffer_size:
                #         break
                #
                # print('------- 3')
                # print(buffer.getvalue())

                print(self.process.stdout.readline())

                continue

            if self.process.returncode != None:
                if self.process.returncode != 0:
                    print('error')
                print('finished')
                break

        print('--------')
        print(stdout.decode('gb2312'))
        print('--------')
        print(stderr)


    def _trans_read(self, trans_cmd):
        self.process = subprocess.Popen(trans_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        buffer_size = 1024
        buffer = BytesIO()

        while True:
            # output = self.process.stdout.readline()
            # if output == '' and self.process.poll() is not None:
            #     break
            # if output:
            #     print(output.strip())


            print('------- 1')
            read_tmp = self.process.stdout.read(buffer_size)
            print('------- 2', len(read_tmp))
            buffer.write(read_tmp)
            if len(read_tmp) < buffer_size and self.process.poll() is not None:
                break

            print('------- 3')
            #print(buffer.getvalue())

            output = buffer.getvalue().replace(b'\r', b'\n').decode('gb2312')

            match_time = re.findall(r'\s+time=(\d+):(\d+):(\d+)\.(\d+)\s+', output)
            if match_time:
                time_h = float(match_time[-1][0])
                time_m = float(match_time[-1][1])
                time_s = float(match_time[-1][2])
                time_ms = float(match_time[-1][3])
                time_done = time_h * 3600 + time_m * 60 + time_s + time_ms * 0.01
                print(time_done)

        print('done')

    def _trans_new_stream(self, trans_cmd):

        # buffer = BytesIO() # not working
        # self.process = subprocess.Popen(trans_cmd, shell=True, stdout=buffer, stderr=subprocess.STDOUT)

        # this works, so stdout need a file handler
        output = open('output.txt','w')

        self.process = subprocess.Popen(trans_cmd, shell=True, stdout=output, stderr=subprocess.STDOUT)

        while True:
            try:
                (stdout, stderr) = self.process.communicate(timeout=1)
            except subprocess.TimeoutExpired as e:
                print('--- tic')
                # output = buffer.getvalue().replace(b'\r', b'\n').decode('gb2312')
                # print(output)
                output.flush()

                with open('output.txt','r') as f:
                    output_data = f.read()

                    match_time = re.findall(r'\s+time=(\d+):(\d+):(\d+)\.(\d+)\s+', output_data)
                    if match_time:
                        time_h = float(match_time[-1][0])
                        time_m = float(match_time[-1][1])
                        time_s = float(match_time[-1][2])
                        time_ms = float(match_time[-1][3])
                        time_done = time_h * 3600 + time_m * 60 + time_s + time_ms * 0.01
                        print(time_done)
                continue

            if self.process.returncode != None:
                if self.process.returncode != 0:
                    pass
                    print('error')
                print('finished')
                break

        # print('--------')
        # print(buffer.getvalue())
        # output = buffer.getvalue().replace(b'\r', b'\n').decode('gb2312')
        # print(output)

        # print('--------')
        # print(stdout.decode('gb2312'))
        # print('--------')
        # print(stderr)



if __name__ == '__main__':
    f = FFmpeg(logging.getLogger())
    #f.trans('ffmpeg -i D:\\Temp\\rouge1_tv_P1080_265_crf.mp4 -f null -')
    #f.trans('ffmpeg -i D:\\Temp\\star.war.4.10s.mp4 -f null -')
    f.trans('ffmpeg -i D:\\Temp\\star.war.4.270s.mp4 -f null -')