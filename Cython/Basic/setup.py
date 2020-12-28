# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:43
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('someloop.pyx'))
