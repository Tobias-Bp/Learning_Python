#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:27:33 2020

@author: cozzetti
"""

"""
b es un alias de a.
Lo copia y apunta al mismo lugar de memoria
Entonces es medio peligroso

En cambio c es una copia entre los index
"""

a = [1,2,3,4,5]
b = a

c = a[0:2]

b.append(45)

print(a)
print(b)
print(c)