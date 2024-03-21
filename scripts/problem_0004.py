# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:07:38 2024

@author: Antoine
"""

import os
import math

from util.util import timing, format_number
from scripts.problem import Problem

class Problem4(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The largest palindromic made from the product of two {len(str(kwargs['upper_bound']))-1}-digits number is {format_number(self.answer)}"
            
    def isPalindrome(self,n):
        string = str(n)
        m=len(string)
        for i in range(math.ceil(m/2)):
            if string[i]!=string[m-i-1]:
                return False
        return True
    
    @timing
    def solve(self, upper_bound):
        L=[]
        for i in range(1,upper_bound):
            for j in range(1,upper_bound):
                pal = i*j
                if self.isPalindrome(pal):
                    L.append(pal)
        return max(L)


if __name__ == '__main__':
    problem = Problem4(upper_bound = 1_000)
    problem.print_problem()