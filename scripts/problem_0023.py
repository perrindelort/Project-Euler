# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:26:46 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem23(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {format_number(self.answer)}"
    
    def get_divisor_list(self,n):
        L = []
        for i in range(1,n//2+1):
            if n%i==0:
                L.append(i)
        return L
    
    def generate_sum_abundant_numbers_list(self,upper_bound):
        abundant_numbers_list = []
        for i in range(upper_bound):
            L = self.get_divisor_list(i)
            if sum(L)>i:
                abundant_numbers_list.append(i)
        n = len(abundant_numbers_list)
        sum_abundant_numbers_list = []
        for i in range(n):
            for j in range(i,n):
                x = abundant_numbers_list[i]+abundant_numbers_list[j]
                if x < upper_bound:
                    sum_abundant_numbers_list.append(x)
        return list(set((sum_abundant_numbers_list)))

    
    @timing
    def solve(self, upper_bound):
        sum_abundant_numbers_list = self.generate_sum_abundant_numbers_list(upper_bound)
        return int(upper_bound*(upper_bound+1)/2 - sum(sum_abundant_numbers_list) - upper_bound)

if __name__ == '__main__':
    problem = Problem23(upper_bound = 28_123)
    problem.print_problem()