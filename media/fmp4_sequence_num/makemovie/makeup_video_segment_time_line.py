# -*- encoding: utf-8 -*-
"""
@File    : makeup_video_segment_time_line.py
@Time    : 2020/3/5 17:54
@Author  : Zhang.Yang
@Email   : ian.zhang.88@outlook.com
@Software: PyCharm
"""
from xml.dom.minidom import parse
from xml.dom.minidom import Document
import os

def parse_mpd_segment_time_line(mpd):
    time_line_list = []

    DOMTree = parse(mpd)
    MPD = DOMTree.documentElement

    Periods = MPD.getElementsByTagName("Period")
    for p in Periods:
        AdaptationSet = p.getElementsByTagName("AdaptationSet")
        for a in AdaptationSet:
            Representation = a.getElementsByTagName("Representation")
            for r in Representation:
                SegmentTemplate = r.getElementsByTagName("SegmentTemplate")
                for s in SegmentTemplate:
                    S = s.getElementsByTagName("S")
                    for SS in S:
                        elem_S = {}
                        if SS.hasAttribute('t'):
                            elem_S['t'] = SS.getAttribute('t')
                        if SS.hasAttribute('d'):
                            elem_S['d'] = SS.getAttribute('d')
                        if SS.hasAttribute('r'):
                            print("!!!!! r")
                            elem_S['r'] = SS.getAttribute('r')

                        time_line_list.append(elem_S)

    return time_line_list

def merge_time_line(time_line_list):
    one_t = False
    DOMTree_new = Document()
    time_line = DOMTree_new.createElement('time_line')

    for t in time_line_list:
        S = DOMTree_new.createElement('S')

        if 't' in t and not one_t:
            S.setAttribute('t', t['t'])
            one_t = True

        if 'd' in t:
            S.setAttribute('d', t['d'])

        if 'r' in t:
            S.setAttribute('r', t['r'])

        time_line.appendChild(S)

    with open("timeline.xml", 'w') as f:
        time_line.writexml(f, addindent="  ", newl="\n")


def main():
    mpd_path = 'vdieo-seg-mpd'
    mpd_files = os.listdir(mpd_path)
    mpd_files = [os.path.join(mpd_path, i) for i in mpd_files]
    # mpd_files = mpd_files[:2]
    time_line_list = []

    for mpd in mpd_files:
        print('mpd:',mpd)
        seg_time_line_list = parse_mpd_segment_time_line(mpd)
        time_line_list.extend(seg_time_line_list)

    merge_time_line(time_line_list)


if __name__ == '__main__':
    main()
