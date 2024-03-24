# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:33:56 2024

@author: Antoine
"""

import os
import math

from util.util import timing, format_number
from scripts.problem import Problem

def generate_primitive_pythagorean_triples(perimeter_max):
    if perimeter_max >=12 :
        pythagorean_triples = {}
        for m in range(2,math.ceil(math.sqrt(1+perimeter_max*4)/2)):
            for n in range(1,m):
                if math.gcd(n,m) == 1 and (n-m)%2 != 0:
                    key = 2*m**2+2*m*n
                    if key > perimeter_max:
                        continue
                    if pythagorean_triples.get(key) == None:
                        pythagorean_triples[key] = 0
                    pythagorean_triples[key] = pythagorean_triples[key] + 1
        return pythagorean_triples
    
class Problem75(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} values of L ≤ {format_number(kwargs['upper_bound'])} for which exactly one integer sided right angle triangle be formed"
            
    
    @timing
    def solve(self, upper_bound):
        pythagorean_triples = generate_primitive_pythagorean_triples(upper_bound)
        sorted_keys = sorted(list(pythagorean_triples.keys()))

        for key in sorted_keys:
            val = 2*key
            while val <= upper_bound:
                if pythagorean_triples.get(val) == None:
                    pythagorean_triples[val] = 1
                else:
                    pythagorean_triples[val] += 1
                val += key
        return list(pythagorean_triples.values()).count(1)


if __name__ == '__main__':
    problem = Problem75(upper_bound = 1_500_000)
    problem.print_problem()