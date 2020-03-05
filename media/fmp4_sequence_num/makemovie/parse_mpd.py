# -*- encoding: utf-8 -*-
"""
@File    : parse_mpd.py
@Time    : 2020/3/5 17:16
@Author  : Zhang.Yang
@Email   : ian.zhang.88@outlook.com
@Software: PyCharm
"""

from xml.dom.minidom import parse
from xml.dom.minidom import Document

def main():
    DOMTree = parse("rogue.mpd")
    MPD = DOMTree.documentElement

    Periods = MPD.getElementsByTagName("Period")
    for p in Periods:
        print('Period id:', p.getAttribute('id'))
        AdaptationSet = p.getElementsByTagName("AdaptationSet")
        for a in AdaptationSet:
            print('AdaptationSet contentType:', a.getAttribute('contentType'))
            Representation = a.getElementsByTagName("Representation")
            for r in Representation:
                SegmentTemplate = r.getElementsByTagName("SegmentTemplate")
                for s in SegmentTemplate:
                    S = s.getElementsByTagName("S")
                    for SS in S:
                        print('-----------------')
                        if SS.hasAttribute('t'):
                            print('S t:', SS.getAttribute('t'))
                        if SS.hasAttribute('d'):
                            print('S d:', SS.getAttribute('d'))
                        if SS.hasAttribute('r'):
                            print('S r:', SS.getAttribute('r'))

    DOMTree_new = Document()
    test = DOMTree_new.createElement('test')

    for i in range(10):
        S = DOMTree.createElement('S')
        test.appendChild(S)

    with open("test.xml", 'w') as f:
        test.writexml(f, addindent="  ", newl="\n")



if __name__ == '__main__':
    main()