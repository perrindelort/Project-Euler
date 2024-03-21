# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:51:21 2024

@author: Antoine
"""

from functools import cache

@cache
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)