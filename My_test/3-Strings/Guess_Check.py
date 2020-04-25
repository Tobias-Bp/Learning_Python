# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:25:27 2020

@author: toto_
"""

###################
# EXAMPLE: guess and check cube root 
###################
cube = 27
#cube = 8120601
for guess in range(abs(cube)+1):
    # passed all potential cube roots
    if guess**3 >= abs(cube):
        # no need to keep searching
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
