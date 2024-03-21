# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:18:32 2024

@author: Antoine
"""

import os
import math

from util.util import timing, format_number
from scripts.problem import Problem

class Problem27(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound_a' not in kwargs.keys():
            raise ValueError("upper_bound_a not specified")
        if 'upper_bound_b' not in kwargs.keys():
            raise ValueError("upper_bound_b not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound_a = kwargs['upper_bound_a'],
                                                  upper_bound_b = kwargs['upper_bound_b'])
        
        self.detailed_answer = f"The maximum number of primes given by the quadratic expression is {format_number(self.answer[1])} and was given by the following coefficients: \na = {format_number(self.answer[2])} b = {format_number(self.answer[3])} hence a x b = {format_number(self.answer[0])}"
        
        # Because we returned 3 values for the detailed_answer
        self.answer = self.answer[0]
    
    def is_prime(self,n):
        if n==1:
            return False
        elif n==2:
            return True
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    
    def max_numbers_of_primes_quad_formula(self,function):
        n=0
        while self.is_prime(abs(function(n))):
            n+=1
        return n
    
    @timing
    def solve(self, upper_bound_a, upper_bound_b):
        max_numbers_of_primes = 0
        best_a = -1000
        best_b = -1000
        for a in range(-upper_bound_a,upper_bound_a):
            for b in range (-upper_bound_b,upper_bound_b+1):
                def f(n):
                    return n**2+a*n+b
                numbers_of_primes = self.max_numbers_of_primes_quad_formula(f)
                if numbers_of_primes > max_numbers_of_primes:
                    max_numbers_of_primes = numbers_of_primes
                    best_a = a
                    best_b = b
        return (best_a*best_b, max_numbers_of_primes, best_a, best_b)


if __name__ == '__main__':
    problem = Problem27(upper_bound_a = 1_000,
                        upper_bound_b = 1_000)
    problem.print_problem()