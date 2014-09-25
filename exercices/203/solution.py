# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 21:16:04 2014

@author: Guillaume
"""


def is_multiple(a, b):
    c = b % a
    if (c == 0) & (c is int):
        return(True)
    else:
        return(False)
