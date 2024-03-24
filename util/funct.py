# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:51:21 2024

@author: Antoine
"""

import math
from collections import Counter
from functools import cache
from primePy import primes
from sympy import isprime
import numpy as np

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

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def is_prime(n):
    return primes.check(n)

def is_prime_for_truncatable_prime(n):
    if n < 11:
        return False
    else:
        return primes.check(n)

def is_truncatable_prime(integer):
    integer_string = str(integer)
    for i in range(1, len(integer_string)):
        if not is_prime_for_truncatable_prime(int(integer_string[i:])):
            return False
    for i in range(1, len(integer_string)):
        if not is_prime_for_truncatable_prime(int(integer_string[:-i])):
            return False
    return True

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

def is_permutation(string1,string2):
    if (len(string1)) == len(string2):
        return Counter(string1) == Counter(string2)
    return False

def is_pan_digital(string):
    if (len(string)!=9):
        return False
    for i in range(1,10):
        if string.count(str(i))!=1:
            return False
    return True

def is_pentagonal(integer):
    if integer != 0:
        n = math.ceil((integer*2/3)**0.5)
        return 0.5*(n*(3*n-1)) == integer
    return False

def is_hexagonal(integer):
    if integer != 0:
        n = math.ceil((integer/2)**0.5)
        return n*(2*n-1) == integer

def load_data_from_txt(problem_number, split = True, sep =',', use_numpy = False):
    problem_number_str = str(problem_number).zfill(4)
    path = f"././data/data/problem_{problem_number_str}.txt"
    if use_numpy:
        return np.loadtxt(path, delimiter = sep)
    file = open(path,'r')
    if split:
        return file.read().split(sep = sep)
    else:
        return file.read()