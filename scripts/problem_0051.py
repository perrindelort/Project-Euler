# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:43:36 2024

@author: Antoine
"""

import os
from sympy import nextprime
from itertools import combinations

from util.util import timing, format_number
from util.funct import isprime
from scripts.problem import Problem

def a(number_string:str) -> set[str]:
    # Enlever les pattern commençant par */0 et ceux finissant par un nombre pair
    n = len(number_string)
    number_string = '*'.join(number_string)
    number_string += '*'
    return combinations(number_string[1:],n-1)

def generate_patterns(s):
    if len(s) == 1:
        return [s]
    else:
        combinations = []
        for c in generate_patterns(s[1:]):
            combinations.append(s[0] + c)
            combinations.append('*' + c)
        return combinations


class Problem51(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        
        self.answer, self.time_taken = self.solve(target = kwargs['target'])
        
        self.detailed_answer = f"The smallest prime that is part of an {format_number(kwargs['target'])} prime value family when replacing is {format_number(self.answer[0])} and its family is {sorted(self.answer[1])}"
            
        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]
        
    @timing
    def solve(self, target):
        prime = 101
        patterns = {}
        while True:
            prime = nextprime(prime, 1)
            prime_string = str(prime)
            prime_patterns = generate_patterns(prime_string)
            prime_patterns = set(prime_patterns)
            is_key = False
            length = len(next(iter(prime_patterns)))
            if patterns.get(length) != None:
                is_key = True
                prime_patterns.difference_update(patterns[length])
                
            for pattern in prime_patterns:
                primes = set()
                digits = "123456789" if pattern[0] in '0*' else "0123456789"
                for digit in digits:
                    number = int(pattern.replace('*',digit))
                    if isprime(number):
                        primes.add(number)
                if len(primes) == target:
                    return min(primes), primes
                
            if is_key:
                patterns[length].update(prime_patterns)
            else:
                patterns[length] = prime_patterns
                
            
        


if __name__ == '__main__':
    problem = Problem51(target = 8)
    problem.print_problem()