# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 16:26
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com]

from threading import Event

class GlobalVar:

    # work_flag=True
    work_flag=Event()
    kill_task_flag=Event()

    transcode_pid = None
    transcode_man_kill = None
    ffmpeg_name = '/usr/local/bin/svc_ffmpeg'

    host_name='host_name'

def reset_kill_task_event():
    GlobalVar.kill_task_flag.clear()

def kill_task():
    GlobalVar.kill_task_flag.set()