# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:35:59 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem28(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'size' not in kwargs.keys():
            raise ValueError("size not specified")
        
        self.answer, self.time_taken = self.solve(size = kwargs['size'])
        
        self.detailed_answer = f"The sum of the numbers on the diagonals of a {kwargs['size']} x {kwargs['size']} spirals formed in the same way is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, size):
        s=1
        last_number = 1
        for i in range(2,size,2):
            for j in range(4):  
                last_number +=i
                s+= last_number
        return s


if __name__ == '__main__':
    problem = Problem28(size = 1_001)
    problem.print_problem()