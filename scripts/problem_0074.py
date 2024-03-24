# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:18:17 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import factorial
from scripts.problem import Problem

class Problem74(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'],
                                                  target = kwargs['target'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} chains with a starting number below {format_number(kwargs['upper_bound'])} that contain exactly {format_number(kwargs['target'])} non-repeating terms"
            
    
    @timing
    def solve(self, upper_bound, target):
        # Bruteforce, to be optimized by using information from previous chains : might be able to do it in less than 10s ?
        factorial_value = {}
        count = 0
        for integer in range(10):
            factorial_value[integer] = factorial(integer)
        for number in range(upper_bound + 1):
            terms = [number]
            number_string = str(number)
            value = 0
            for digit in number_string:
                value += factorial_value[int(digit)]
            if value not in terms:
                terms.append(value)
            stop = False
            while not stop:
                number_string = str(terms[-1])
                value = 0
                for digit in number_string:
                    value += factorial_value[int(digit)]
                if value not in terms:
                    terms.append(value)
                else:
                    stop = True
            if len(terms) == target:
                count += 1
        return count


if __name__ == '__main__':
    problem = Problem74(upper_bound = 1_000_000,
                        target = 60)
    problem.print_problem()