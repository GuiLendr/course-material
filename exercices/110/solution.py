# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:03:07 2014

@author: Guillaume
"""

import sys
if len(sys.argv) == 1:
    m = "usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number"
    print(m)
elif len(sys.argv) == 4:
    a = int(sys.argv[1])
    b = sys.argv[2]
    c = int(sys.argv[3])
    res = 0
    if (c == 0):
        print("input error")
    elif (b == "+"):
        res = a + c
    elif (b == "-"):
        res = a - c
    elif (b == "*"):
        res = a * c
    elif (b == "%"):
        res = a % c
    elif (b == "^"):
        res = pow(a, c)
    else:
        print("input error")
    print(res)
