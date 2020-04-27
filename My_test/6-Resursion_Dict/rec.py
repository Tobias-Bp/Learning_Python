#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:51:57 2020

@author: cozzetti
"""
def fact(number):
    if(number == 1):
        print(number,"=")
        return 1
    else:
        print(number,"*")
        return(number*fact(number-1))

n = int(input("Enter a number:"))
print(n,"! = ")
f=fact(n)
print(f)