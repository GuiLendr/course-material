# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:05:30 2014

@author: Guillaume
"""


import string
alph = string.ascii_lowercase
lettre = list(alph)
for i in alph :
    for j in alph :
        if(i != j) :
            if(i < j) :
                print(i+j, "\n")
