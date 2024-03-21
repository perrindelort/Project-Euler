# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:51:21 2024

@author: Antoine
"""

from functools import cache

@cache
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def load_data_from_txt(problem_number, split = True, sep =','):
    problem_number_str = str(problem_number).zfill(4)
    path = f"././data/data/problem_{problem_number_str}.txt"
    file = open(path,'r')
    if split:
        return file.read().split(sep = sep)
    else:
        return file.read()