# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:38:13 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class ProblemXXX(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'arg' not in kwargs.keys():
            raise ValueError("arg not specified")
        
        self.answer, self.time_taken = self.resolution(arg = kwargs['arg'])
        
        self.detailed_answer = f" is {format_number(self.answer)}"
            
    
    @timing
    def resolution(self, **kwargs):
        pass


if __name__ == '__main__':
    problem = ProblemXXX()
    problem.print_problem()