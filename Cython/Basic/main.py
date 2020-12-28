# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:34
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import time
from someloop import cloop

def pythonloop(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

start = time.time()
pythonloop(99999999)
print("pythonloop time",time.time()-start)

start = time.time()
cloop(99999999)
print("cloop time",time.time()-start)



"""
For variables we have:
cdef int a, b, c
cdef char *s
cdef float x = 0.5 (single precision)
cdef double x = 63.4 (double precision)
cdef list names
cdef dict goals_for_each_play
cdef object card_deck

Notice how all of these types come from C/C++! For the functions we have:
def — regular python function, calls from Python only.
cdef — Cython only functions which can’t be accessed from python-only code i.e must be called within Cython
cpdef — C and Python. Can be accessed from both C and Python


python setup.py build_ext --inplace
"""