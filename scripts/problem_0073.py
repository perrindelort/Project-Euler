# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:48:01 2024

@author: Antoine
"""

import os
from math import gcd

from util.util import timing, format_number
from scripts.problem import Problem

class Problem73(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} fractions lying between 1/2 and 1/3 in the sorted set of reduced proper fractions for d ≤ {format_number(kwargs['upper_bound'])}"
            
    
    @timing
    def solve(self, upper_bound):
        count = 0
        for d in range(2, upper_bound + 1):
            for n in range(1,d):
                val = n/d
                if 1/3 < val < 1/2:
                    if gcd(n,d) == 1:
                        count += 1
        return count


if __name__ == '__main__':
    problem = Problem73(upper_bound = 12_000)
    problem.print_problem()