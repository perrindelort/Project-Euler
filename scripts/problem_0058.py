# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:50:12 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem
from primePy import primes

class Problem58(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        
        self.answer, self.time_taken = self.solve(target = kwargs['target'])
        
        self.detailed_answer = f" the side length of the square spiral for which the ratio of primes along both diagonals first falls below {format_number(kwargs['target'])} %  is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, target):
        target_percentage = target / 100
        diag1 = [3,7]
        diag2 = [5,9]
        diag_size = 4
        prime_count = 3
        length_minus = 4
        while True:
            for iteration in range(2):
                number1 = diag2[-1]+length_minus
                diag1.append(number1)
                number2 = diag1[-1]+length_minus
                diag2.append(number2)
                if primes.check(number1):
                    prime_count += 1
                if primes.check(number2):
                    prime_count += 1
            diag_size += 4
            if prime_count/diag_size < target_percentage:
                return length_minus-1
            length_minus += 2


if __name__ == '__main__':
    problem = Problem58(target = 10)
    problem.print_problem()