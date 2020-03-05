# -*- encoding: utf-8 -*-
"""
@File    : extract-dash-seg.py
@Time    : 2020/2/28 11:53
@Author  : Zhang.Yang
@Email   : ian.zhang.88@outlook.com
@Software: PyCharm
"""

import os, subprocess, shutil

input_mp4 = 'input-mp4'
output_dir = 'input'
dash_temp_dir = 'dash-temp'
seg_name = 'video-{:05d}.m4s'
vdieo_seg_mpd_dir = 'vdieo-seg-mpd'

file_num = 0
mpd_num = 0

ffmpeg_cmd = 'ffmpeg -i {input} -c copy -f dash -media_seg_name "video-$Number%05d$.m4s" {out_dir}/video.mpd'

for mp4 in os.listdir(input_mp4):
    shutil.rmtree(dash_temp_dir)
    os.mkdir(dash_temp_dir)
    file = input_mp4+'/'+mp4
    cmd = ffmpeg_cmd.format(input=file, out_dir=dash_temp_dir)
    subprocess.call(cmd, shell=True)

    # # extract m4s files
    # m4s_file = [i for i in os.listdir(dash_temp_dir) if 'm4s' in i]
    #
    # for i in m4s_file:
    #     file_num+=1
    #     src = os.path.join(dash_temp_dir, i)
    #     dst = os.path.join(output_dir, seg_name.format(file_num))
    #     shutil.move(src,dst)

    # extract mpd files
    mpd_num+=1
    src = os.path.join(dash_temp_dir, 'video.mpd')
    dst = os.path.join(vdieo_seg_mpd_dir, 'video'+'%05d'%mpd_num+'.mpd')
    shutil.move(src,dst)






