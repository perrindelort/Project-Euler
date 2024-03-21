# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:49:29 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem1(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        self.answer, self.time_taken = self.resolution(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The sum of all the multiples of 3 or 5 below {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"
            
    
    @timing
    def resolution(self, upper_bound):
        s = 0
        for n in range(upper_bound):
            if n%3==0 or n%5==0:
                s+=n
        return s


if __name__ == '__main__':
    problem = Problem1(upper_bound = 5_000)
    problem.print_problem()