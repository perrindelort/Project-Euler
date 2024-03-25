# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:02:43 2024

@author: Antoine
"""

import os
from util.util import timing, format_number
from scripts.problem import Problem

def add_digits_squared(number):
    s = 0
    for digit in str(number):
        s += int(digit)**2
    return s


class Problem92(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} starting numbers below {format_number(kwargs['upper_bound'])} that will arrive at 89"
            
    
    @timing
    def solve(self, upper_bound):
        death_loop = {1 : 1, 89 : 89}
        occurences = {1: 0, 89 : 0}
        ends = [1,89]
        for number in range(1, 1000):
            val = add_digits_squared(number)
            while val not in ends:
                val = add_digits_squared(val)
            occurences[val] += 1
            death_loop[number] = val
        for number in range(1_001, upper_bound):
            val = add_digits_squared(number)
            while death_loop.get(val) == None:
                val = add_digits_squared(val)
            occurences[death_loop[val]] += 1
            death_loop[number] = death_loop[val]
        return occurences[89]


if __name__ == '__main__':
    problem = Problem92(upper_bound = 10_000_000)
    problem.print_problem()