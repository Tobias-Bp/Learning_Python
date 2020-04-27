#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:57:39 2020

@author: cozzetti
"""

a_list = []    #Empty

l = ['t','o','b','i','a','s']

for i in l:
    print(ord(i))
    
for i in range(len(l)):
    l[i] = chr(ord(l[i])+1)
    print(l[i])