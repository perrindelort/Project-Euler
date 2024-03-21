# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:53:44 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import fibonacci
from scripts.problem import Problem

class Problem25(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The the first term of the Fibonnaci sequence that contains than {format_number(kwargs['upper_bound'])} digits is {format_number(self.answer[1])} and its index is {format_number(self.answer[0])}"
           
        # Because we returned 2 values for detailed_answer
        self.answer = self.answer[0]
        

    def nextFibo(self,fn_1,fn_2):
        return fn_1+fn_2
    
    @timing
    def solve(self, upper_bound):
        fn_2 = 1
        fn_1 = 1
        index = 2
        while len(str(fn_1))!=upper_bound:
            fn_1,fn_2 = self.nextFibo(fn_1,fn_2),fn_1
            index+=1
        return index,fn_1



if __name__ == '__main__':
    problem = Problem25(upper_bound = 1_000)
    problem.print_problem()

