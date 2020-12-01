# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 19:13
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import ray
import subprocess

ray.init(address="10.19.17.188:6379",  _redis_password='5241590000000000')


@ray.remote
def ls():
    return subprocess.check_output("ls /opt/",shell=True)

futures = ls.remote()
print(ray.get(futures))
