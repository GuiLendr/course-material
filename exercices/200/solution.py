# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 20:10:30 2014

@author: Guillaume
"""


def is_prime(num):
    if ((num == 0) | (num == 1)):
        return ("False")
    else:
        racine = int(pow(num, 0.5))
        for div in range(2, racine):
            if num % div == 0:
                return ("False")
            div = div + 1
        return("True")
