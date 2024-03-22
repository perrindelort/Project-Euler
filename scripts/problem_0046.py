# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:00:59 2024

@author: Antoine
"""

import os
import math
from primePy import primes

from util.util import timing, format_number
from scripts.problem import Problem

def is_twice_time_a_square(integer,prime):
    new_integer = integer - prime
    for square_root in range(1,math.ceil(math.sqrt(integer))):
        if 2*((square_root)**2) == new_integer:
            return True
    return False

class Problem46(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, upper_bound):
        prime_list = primes.upto(upper_bound)
        for integer in range(33,upper_bound+1,2):
            is_true = False
            if primes.check(integer) == False:
                for index in range(len(prime_list)):
                    new_integer = integer - prime_list[index]
                    if is_twice_time_a_square(integer,prime_list[index]):
                        is_true = True
                        break
                    if new_integer < 0:
                        break
                if is_true == False:
                    return integer

if __name__ == '__main__':
    problem = Problem46(upper_bound = 10_000)
    problem.print_problem()