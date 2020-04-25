# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:45:58 2020

@author: toto_
"""


###################
# EXAMPLE: bisection cube root (only positive cubes!)
###################
#cube = 27
cube = 1/3
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
if(cube < 1): #Así fijo el límite superior
    #una raiz < 1 siempre es <1    
    high = 1
    low = 0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)