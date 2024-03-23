# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:22:52 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

def is_palindrome(number):
    string = str(number)
    reverse_string = string[::-1]
    if reverse_string == string:
        return True
    return False

def is_lychrel(number):
    n = number
    for iteration in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True


class Problem55(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} Lychrel numbers below {format_number(kwargs['upper_bound'])}"
            
    
    @timing
    def solve(self, upper_bound):
        count = 0
        for number in range (upper_bound + 1):
            if is_lychrel(number):
                count += 1
        return count


if __name__ == '__main__':
    problem = Problem55(upper_bound = 10_000)
    problem.print_problem()