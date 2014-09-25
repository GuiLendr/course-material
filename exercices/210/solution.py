# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 19:37:49 2014

@author: Guillaume
"""

import is_prime

nombres_premiers = []
nombres_premiers.append(2)
nombres_impairs = []

for i in range(3, 999):
    if i % 2 != 0:
        nombres_impairs.append(i)
print(nombres_impairs)
for nb in range(3, len(nombres_impairs)):
    res = is_prime.is_prime(nb)
    if res is True:
        nombres_premiers.append(nb)
    nb = nb + 1
print(nombres_premiers)
