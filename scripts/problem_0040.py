# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:13:55 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem40(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The value of d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000 is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, upper_bound):
        champernowne_constant = ""
        integer = 1
        while len(champernowne_constant) < upper_bound :
            champernowne_constant += str(integer)
            integer += 1
        value = 1
        i = 1
        for i in range(7):
            value = value * int(champernowne_constant[10**i-1])
            i = i*10
        return value


if __name__ == '__main__':
    problem = Problem40(upper_bound = 1_000_000)
    problem.print_problem()