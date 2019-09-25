# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:39
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from hdfs import Config
from hdfs import InsecureClient

#Init
myClient = InsecureClient('http://snn1.heracles.sohuno.com:50070;http://snn2.heracles.sohuno.com:50070', 'sohuvideo', root='/user/sohuvideo')

#List HDFS file
print(myClient.list('/user/sohuvideo/'))

#Upload file to HDFS, localsource=/tmp/gmond.log, HDFSdest=/user/sohuvideo/
myClient.upload('/user/sohuvideo/test/', 'd:/Temp/star.war.4.270s.mp4')

#Download file from HDFS, source=/user/sohuvideo/testfile, localpath=tmp
myClient.download('/user/sohuvideo/test/star.war.4.270s.mp4', './')


print(myClient.list('/user/sohuvideo/test'))

