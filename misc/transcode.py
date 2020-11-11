# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 15:42
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import subprocess
from concurrent.futures import ThreadPoolExecutor

def read_file():
    name_list = []

    with open('filename.txt','r') as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            name_list.append(l)

    return name_list

def trans_thread(src, dst):
    trans_cmd = f'ffmpeg -i {src} -preset slower -crf 21 -c:a aac -ar 48000 -ac 2 -b:a 96k {dst}'

    ret = subprocess.call(trans_cmd, shell=True)

    if ret != 0:
        return dst, f"error in {dst}, cmd:{trans_cmd}"

    return dst, "done"

def main():
    name_list = read_file()

    base_path = '/HUGE/MediaLib/000/019/000019719/'

    pool = ThreadPoolExecutor(5)
    results = []

    for name in name_list:
        full_path = base_path+name
        results.append(pool.submit(trans_thread,full_path,name))

    out_log = open('trans_log.log','w')
    for r in results:
        name, msg = r.result()
        print(name, msg)
        out_log.write('%s %s\n' % (name, msg))
        out_log.flush()

    out_log.close()

if __name__ == "__main__":
    main()