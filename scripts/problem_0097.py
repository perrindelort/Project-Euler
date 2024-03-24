# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:38:04 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem97(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'factor' not in kwargs.keys():
            raise ValueError("factor not specified")
            
        if 'base' not in kwargs.keys():
            raise ValueError("base not specified")
            
        if 'exponent' not in kwargs.keys():
            raise ValueError("exponent not specified")
            
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        
        self.answer, self.time_taken = self.solve(factor = kwargs['factor'],
                                                  base = kwargs['base'],
                                                  exponent = kwargs['exponent'],
                                                  target = kwargs['target'])
        
        self.detailed_answer = f"The last {format_number(kwargs['target'])} digits of {format_number(kwargs['factor'])} x {format_number(kwargs['base'])}^{format_number(kwargs['exponent'])} are {format_number(self.answer)}"
            
    
    @timing
    def solve(self, factor, base, exponent, target):
        return (factor * pow(base, exponent, target**target) + 1) % target**target


if __name__ == '__main__':
    problem = Problem97(factor = 28_433, 
                        base = 2,
                        exponent = 7_830_457,
                        target = 10)
    problem.print_problem()