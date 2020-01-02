# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 11:06
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import fnmatch
import shutil
import os

input = 'output'
output = 'output-mp4'
exclude = ['*.yuv','vmaf_compare*']

for dirpath, dirnames, filenames in os.walk(input):

    out_dir = dirpath.replace(input, output)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for f in filenames:
        found_exclude_match = False
        for exc in exclude:
            if fnmatch.fnmatch(f, exc):
                found_exclude_match = True
                break

        if found_exclude_match:
            continue

        shutil.copy(os.path.join(dirpath,f), os.path.join(out_dir, f))


