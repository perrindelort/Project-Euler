# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:26:50 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem48(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The last 10 digits of the serie 1^1 + 2^2 + 3^3 + ... + {format_number(kwargs['upper_bound'])}^{format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        s = 0
        for i in range(1,1001):
            s += i**i
        sum_string = str(s)
        return int(sum_string[len(sum_string)-10:])


if __name__ == '__main__':
    problem = Problem48(upper_bound = 1_000)
    problem.print_problem()