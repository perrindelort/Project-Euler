# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:37:22 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import is_pentagonal
from scripts.problem import Problem

class Problem44(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The value of D is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        pentagonal_numbers_list = [1,5]
        n = 2
        while True:
            for pentagonal_number in pentagonal_numbers_list:
                if is_pentagonal(pentagonal_numbers_list[-1] - pentagonal_number):
                    if is_pentagonal(pentagonal_numbers_list[-1] + pentagonal_number):
                        return int(pentagonal_numbers_list[-1] - pentagonal_number)
            n += 1
            pentagonal_numbers_list.append(0.5*(n*(3*n-1)))


if __name__ == '__main__':
    problem = Problem44()
    problem.print_problem()