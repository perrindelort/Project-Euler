# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:50:17 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import is_palindrome
from scripts.problem import Problem

class Problem36(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The sum of all numbers < {format_number(kwargs['upper_bound'])} that are palindromic in base 2 and 10 is {format_number(self.answer)}"
       
    
    
    @timing
    def solve(self, upper_bound):
        is_palindrome_in_both_base = []
        for integer in range(1,upper_bound+1):   
            if is_palindrome(str(integer)):
                if is_palindrome(bin(integer)[2:]):
                    is_palindrome_in_both_base.append(integer)
        return sum(is_palindrome_in_both_base)


if __name__ == '__main__':
    problem = Problem36(upper_bound = 1_000_000)
    problem.print_problem()