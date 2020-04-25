# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:07:06 2020

@author: toto_
"""


s = input("Write a word: ")
m = input("Write a word: ")

for char in s:
    if (char == 'a' or char == 'e'):
        print("There is an a or e")
        
# =============================================================================
# Ese tipo de for itera sobre el string
# =============================================================================

for char in s:
    if char in m:
        print(char,"includede in",m)
# =============================================================================
# in devuelve true si lo pedido está en el objeto
# =============================================================================
