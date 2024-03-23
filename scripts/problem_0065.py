# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:25:11 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem65(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'term_number' not in kwargs.keys():
            raise ValueError("term_number not specified")
        
        self.answer, self.time_taken = self.solve(term_number = kwargs['term_number'])
        
        self.detailed_answer = f"The sum of the digits in the numerator of the {format_number(kwargs['term_number'])}th term of the continued fraction for e is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, term_number):
        numbers = [2]
        k = 1
        while len(numbers) < term_number:
            numbers.append(1)
            numbers.append(2*k)
            numbers.append(1)
            k += 1 
        while len(numbers) > term_number:
            numbers.remove(numbers[-1])
        numerator = 1
        denominator = numbers.pop()
        for number in numbers[::-1]:
            denominator, numerator = denominator * number + numerator, denominator
        numerator_string = str(denominator)
        return sum([int(digit) for digit in numerator_string])


if __name__ == '__main__':
    problem = Problem65(term_number = 100)
    problem.print_problem()