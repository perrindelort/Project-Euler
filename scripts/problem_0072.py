# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:42:31 2024

@author: Antoine
"""

import os
from primePy import primes
from math import gcd

from util.util import timing, format_number
from scripts.problem import Problem

def calc_phi(n):
    factors = list(set(primes.factors(n)))
    p = n
    for factor in factors:
        p*=(1-1/factor)
    return int(p)

class Problem72(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} elements in the set of reduced proper fractions for d ≤ {format_number(kwargs['upper_bound'])}"
            
    
    @timing
    def solve(self, upper_bound):
        count = 0
        for d in range(2, upper_bound + 1):
            count += calc_phi(d)
        return count


if __name__ == '__main__':
    problem = Problem72(upper_bound = 1_000_000)
    problem.print_problem()