# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:52:18 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem6(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer =f"The difference between the sum of the squares of the first {format_number(kwargs['upper_bound'])} natural numbers and the square of the sum is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, upper_bound):
        s1=0
        s2=0
        for i in range(upper_bound + 1):
            s1+=i**2
            s2+=i
        s2=s2**2
        return s2-s1


if __name__ == '__main__':
    problem = Problem6(upper_bound = 100)
    problem.print_problem()