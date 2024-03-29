# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:52:11 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem9(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        
        self.answer, self.time_taken = self.solve(target = kwargs['target'])
        
        self.detailed_answer = f"The value of the products a•b•c where (a,b,c) is the only pythagorean triplet s.t. a+b+c={format_number(kwargs['target'])} is {format_number(self.answer[0])} with a = {format_number(self.answer[1])}, b = {format_number(self.answer[2])}, c = {format_number(self.answer[3])} "
            
        self.answer = self.answer[0]
    @timing
    def solve(self, target):
        for c in range(2,target):
            for b in range(c):
                for a in range(b):
                    if (a**2+b**2==c**2):
                        if (a+b+c==target):
                            return (a*b*c, a, b, c)
                        


if __name__ == '__main__':
    problem = Problem9(target = 1_000)
    problem.print_problem()