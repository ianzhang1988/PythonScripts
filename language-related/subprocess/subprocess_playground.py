# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 16:33
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import subprocess

print('begin')
output = None
try:
    output = subprocess.check_output(['ffmpeg.exe'], stderr=subprocess.PIPE)
except subprocess.CalledProcessError as e:

    print(e.returncode)
    print('+++++++++')
    print(e.stderr.decode('gb2312'))
    print('=========')
    print(e.stdout)
    output = e.output

    print(e)

print('---------------')
if output:
    print(output.decode('gb2312'))