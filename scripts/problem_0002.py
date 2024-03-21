# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:57:59 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem


class Problem2(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upperbound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The sum of even-valued Fibonacci terms that does not exceed {format_number(kwargs['upper_bound'])} is {format_number(self.answer)}"
    
    
    def fibonacci(n):
        L=[1,2]
        fibo_n2=1
        fibo_n1=2
        for i in range(n-2):
            fibo_n1,fibo_n2 = fibo_n1+fibo_n2,fibo_n1
            L.append(fibo_n1)
        return L
    
    @timing
    def solve(self, upper_bound):
        s=2
        fibo_n2=1
        fibo_n1=2
        while s < upper_bound:
            fibo_n1,fibo_n2 = fibo_n1+fibo_n2,fibo_n1
            if fibo_n1%2==0:
                s+=fibo_n1
        return s


if __name__ == '__main__':
    problem = Problem2(upper_bound = 4_000_000)
    problem.print_problem()

