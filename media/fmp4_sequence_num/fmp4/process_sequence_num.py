# -*- encoding: utf-8 -*-
"""
@File    : process_sequence_num.py
@Time    : 2020/2/25 14:42
@Author  : Zhang.Yang
@Email   : ian.zhang.88@outlook.com
@Software: PyCharm
"""

from pymp4.parser import Box
import os

class ProcessSequenceNum:
    def __init__(self):
        self.boxes = []
        self.current_sequence_num = 0

    def set_start_sequence_num(self, num):
        self.current_sequence_num = num

    def read_mp4_file(self, file):

        with open(file, 'rb') as f:
            data = f.read()

        self.boxes = []
        processed_byte = 0
        data_lenth = len(data)
        while True:
            if processed_byte >= data_lenth:
                break

            b = Box.parse(data[processed_byte:])
            self.boxes.append(b)

            processed = b.end
            processed_byte += processed

    def write_modified_mp4_file(self, path):
        for b in self.boxes:
            if b.type != b'moof':
                continue

            for c in b.children:
                if c.type == b'mfhd':
                    c.sequence_number = self.current_sequence_num
                    self.current_sequence_num+=1
                    break

        with open(path, 'wb') as f:
            for b in self.boxes:
                # if b.type in [b'mfra']:
                #     continue
                data = Box.build(b)
                f.write(data)

def main():
    prcsSeqNum = ProcessSequenceNum()
    prcsSeqNum.set_start_sequence_num(1)

    file_name = ['frag1.m4s', 'frag2.m4s', 'frag3.m4s']
    input = [os.path.join('input', i) for i in file_name]
    output = [os.path.join('ouput', 'seq-'+i) for i in file_name]

    for i, o in zip(input, output):
        prcsSeqNum.read_mp4_file(i)
        prcsSeqNum.write_modified_mp4_file(o)


if __name__ == '__main__':
    main()
