#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:30:03 2020

@author: cozzetti
"""

my_dict = {"Boca":6,"Bojo":7,"riBer":4,"Velesh":1}

my_dict["Casla"] = 1
print(my_dict["Boca"])

for name in my_dict:
    print(my_dict[name])
    
print(my_dict.keys())
print(my_dict.values())