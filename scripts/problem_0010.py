# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:56:17 2024

@author: Antoine
"""

import os
import math

from util.util import timing, format_number
from scripts.problem import Problem

class Problem10(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The sum of all primes below {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"
        
    def isPrime(self,n):
        if n==1:
            return False
        elif n==2:
            return True
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    
    @timing
    def solve(self, upper_bound):
        s=2
        for i in range(3,upper_bound,2):
            if self.isPrime(i):
                s+=i
        return s


if __name__ == '__main__':
    problem = Problem10(upper_bound = 2_000_000)
    problem.print_problem()