# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:43:12 2020

@author: toto_
"""

table = int(input("Table number:"))
for i in range(10):
    print(table,"*",i,"\t=\t",table*i)

#Range hace arrancar en 0 y terminar en 9, tiene 10 pasos

#range(start,stop,step)
    
number = int(input("Table number:"))
for i in range(0,5,1):
    print(number,"*",i,"\t=\t",number*i)
    if ( (number*i)%2):
        break
    
#Salgo en caso de que la multiplicaion sea impar
    
    
    


