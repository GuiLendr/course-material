# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:04:01 2014

@author: Guillaume
"""


def fibo(num):
    liste = []
    liste.append(1)
    liste.append(2)
    for n in range(2, num):
        fibo_n = liste[n - 1] + liste[n - 2]
        liste.append(fibo_n)
    return liste

res = fibo(10)
print(res)
