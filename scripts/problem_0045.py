# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:41:21 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import is_pentagonal, is_hexagonal
from scripts.problem import Problem

class Problem45(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The next triangle number that is also pentagonal and hexagonal is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        n = 285
        triangle_number = n*(n+1)/2
        stop = False
        while stop == False:
            n += 1
            triangle_number += n
            if is_pentagonal(triangle_number) and is_hexagonal(triangle_number):
                stop = True
        return triangle_number


if __name__ == '__main__':
    problem = Problem45()
    problem.print_problem()