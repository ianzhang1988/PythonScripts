# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:39
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from hdfs import Config
from hdfs import InsecureClient

#Init
myClient = InsecureClient('http://127.0.0.1:50070;http://127.0.0.150070', 'video', root='/user/video')

#List HDFS file
print(myClient.list('/user/video/'))

#Upload file to HDFS, localsource=/tmp/gmond.log, HDFSdest=/user/video/
myClient.upload('/user/video/test/', 'd:/Temp/star.war.4.270s.mp4')

#Download file from HDFS, source=/user/sohuvideo/testfile, localpath=tmp
myClient.download('/user/video/test/star.war.4.270s.mp4', './')


print(myClient.list('/user/video/test'))

