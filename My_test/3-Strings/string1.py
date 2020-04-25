# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:33:18 2020

@author: toto_
"""

s1 = input("Type:")
s2 = input("Type:")
print("\n",s1,"has",len(s1),"characters")
print(s2,"has",len(s2),"characters")

if s1==s2:
    print("The strings are the same☻")
    
    
print(s1[0:len(s1)-1:1],"\n")
# =============================================================================
# Ese [] es como indexar, como se hace en un for.
#[start:stop:step]
# =============================================================================
print(s2[0:len(s2)-2:2],"\n")

print(s2[::-1]) 
# Esto lo da vuelta al stringk