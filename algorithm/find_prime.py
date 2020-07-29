#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 21:03
# @Author  : Ian.Zhang
# @Email   : ian.zhang.88@outlook.com
# @File    : find_prime.py

import math

def is_prime(i):
    sub_i = int(math.sqrt(i))
    for j in range(2, sub_i + 1):
        if (i % j) == 0:
            return False
    return True

def find_prime(n):
    for i in range(n):
        if is_prime(i):
            print(i)

# find_prime(100)

# https://stackoverflow.com/questions/453793/which-is-the-fastest-algorithm-to-find-prime-numbers

# https://en.wikipedia.org/wiki/Sieve_of_Atkin
# http://cr.yp.to/primegen.html

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes too much space
def Sieve_of_Eratosthenes(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

print(Sieve_of_Eratosthenes(100))

